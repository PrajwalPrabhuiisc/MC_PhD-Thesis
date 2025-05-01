import open3d as o3d

def visualize_point_cloud(pcd, colors):
    pcd.colors = o3d.utility.Vector3dVector(colors)
    
    # Optional: Save the point cloud for future use
    # o3d.io.write_point_cloud("output/processed_point_cloud.ply", pcd)
    
    o3d.visualization.draw_geometries([pcd], width=800, height=600)
