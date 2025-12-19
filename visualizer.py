import streamlit as st
import cv2
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import pandas as pd

def display_results(original, annotated, detections, is_video=False):
    """Display original and annotated images/videos side by side."""
    
    if is_video:
        st.subheader("Video Processing Complete")
        st.success(f"Detected {len(detections)} weeds across all frames")
        
        # Display video playback
        st.video(annotated)
        
        # Download button
        with open(annotated, 'rb') as f:
            st.download_button(
                label="⬇️ Download Annotated Video",
                data=f,
                file_name="weed_detection_output.mp4",
                mime="video/mp4"
            )
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Original Image")
            # Convert BGR to RGB for display
            original_rgb = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
            st.image(original_rgb, use_container_width=True)
        
        with col2:
            st.subheader("Detection Results")
            # Convert BGR to RGB for display
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            st.image(annotated_rgb, use_container_width=True)
        
        # Display detection count
        st.metric("Total Weeds Detected", len(detections))

def display_statistics(detections):
    """Display statistics and visualizations of detections."""
    
    if not detections:
        st.warning("No weeds detected in the image/video.")
        return
    
    st.subheader("📊 Detection Statistics")
    
    # Create dataframe
    df = pd.DataFrame(detections)
    
    # Overall metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Detections", len(detections))
    
    with col2:
        avg_confidence = df['confidence'].mean() * 100
        st.metric("Avg Confidence", f"{avg_confidence:.1f}%")
    
    with col3:
        max_confidence = df['confidence'].max() * 100
        st.metric("Max Confidence", f"{max_confidence:.1f}%")
    
    with col4:
        min_confidence = df['confidence'].min() * 100
        st.metric("Min Confidence", f"{min_confidence:.1f}%")
    
    # Confidence distribution
    st.subheader("Confidence Score Distribution")
    
    fig_hist = px.histogram(
        df,
        x='confidence',
        nbins=20,
        title='Distribution of Confidence Scores',
        labels={'confidence': 'Confidence Score', 'count': 'Frequency'},
        color_discrete_sequence=['#2E7D32']
    )
    fig_hist.update_layout(showlegend=False)
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # Confidence over detections (line chart showing confidence for each detection)
    st.subheader("Confidence Scores Across Detections")
    
    df_indexed = df.copy()
    df_indexed['Detection Number'] = range(1, len(df) + 1)
    
    fig_line = px.line(
        df_indexed,
        x='Detection Number',
        y='confidence',
        title='Confidence Score for Each Detection',
        labels={'confidence': 'Confidence Score', 'Detection Number': 'Detection #'},
        markers=True
    )
    fig_line.update_traces(line_color='#2E7D32', marker=dict(size=8))
    fig_line.update_layout(showlegend=False)
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Confidence range breakdown
    st.subheader("Confidence Range Breakdown")
    
    # Create confidence ranges
    bins = [0, 0.3, 0.5, 0.7, 0.9, 1.0]
    labels = ['0-30%', '30-50%', '50-70%', '70-90%', '90-100%']
    df['confidence_range'] = pd.cut(df['confidence'], bins=bins, labels=labels, include_lowest=True)
    
    range_counts = df['confidence_range'].value_counts().sort_index()
    
    fig_bar = px.bar(
        x=range_counts.index.astype(str),
        y=range_counts.values,
        title='Number of Detections by Confidence Range',
        labels={'x': 'Confidence Range', 'y': 'Number of Detections'},
        color=range_counts.values,
        color_continuous_scale='Greens'
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Bounding box size distribution
    st.subheader("Detection Area Distribution")
    
    # Calculate bounding box areas
    df['bbox_area'] = df['bbox'].apply(lambda x: (x[2] - x[0]) * (x[3] - x[1]))
    
    fig_area = px.histogram(
        df,
        x='bbox_area',
        nbins=20,
        title='Distribution of Detection Areas (pixels²)',
        labels={'bbox_area': 'Area (pixels²)', 'count': 'Frequency'},
        color_discrete_sequence=['#558B2F']
    )
    fig_area.update_layout(showlegend=False)
    st.plotly_chart(fig_area, use_container_width=True)
    
    # Summary statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Confidence Statistics")
        stats_df = pd.DataFrame({
            'Metric': ['Mean', 'Median', 'Std Dev', 'Min', 'Max'],
            'Value': [
                f"{df['confidence'].mean()*100:.2f}%",
                f"{df['confidence'].median()*100:.2f}%",
                f"{df['confidence'].std()*100:.2f}%",
                f"{df['confidence'].min()*100:.2f}%",
                f"{df['confidence'].max()*100:.2f}%"
            ]
        })
        st.dataframe(stats_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("📏 Area Statistics")
        area_stats_df = pd.DataFrame({
            'Metric': ['Mean Area', 'Median Area', 'Min Area', 'Max Area'],
            'Value (pixels²)': [
                f"{df['bbox_area'].mean():.0f}",
                f"{df['bbox_area'].median():.0f}",
                f"{df['bbox_area'].min():.0f}",
                f"{df['bbox_area'].max():.0f}"
            ]
        })
        st.dataframe(area_stats_df, use_container_width=True, hide_index=True)
    
    # Detailed detection table
    with st.expander("📋 View Detailed Detection Data"):
        # Format the dataframe for display
        display_df = df.copy()
        display_df['confidence'] = display_df['confidence'].apply(lambda x: f"{x*100:.2f}%")
        display_df['bbox'] = display_df['bbox'].apply(lambda x: f"({x[0]:.0f}, {x[1]:.0f}, {x[2]:.0f}, {x[3]:.0f})")
        display_df['bbox_area'] = display_df['bbox_area'].apply(lambda x: f"{x:.0f}")
        display_df['Detection #'] = range(1, len(display_df) + 1)
        
        st.dataframe(
            display_df[['Detection #', 'confidence', 'bbox', 'bbox_area']].rename(columns={
                'confidence': 'Confidence',
                'bbox': 'Bounding Box (x1, y1, x2, y2)',
                'bbox_area': 'Area (pixels²)'
            }),
            use_container_width=True,
            height=400
        )
        
        # Download CSV
        csv = df[['confidence', 'bbox', 'bbox_area']].to_csv(index=False)
        st.download_button(
            label="⬇️ Download Detection Data (CSV)",
            data=csv,
            file_name="weed_detections.csv",
            mime="text/csv"
        )