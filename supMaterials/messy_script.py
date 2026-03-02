arcpy.sa.ZonalStatisticsAsTable(
    in_zone_data="Charlotte_Mecklenburg_Tree_Canopy",
    zone_field="Geography_",
    in_value_raster="charlotte-north-carolina_af_temp_f.tif",
    out_table=r"C:\Users\lgtateos\Downloads\rawgraphs_data\Charlotte_Mecklenburg_Tree_Canopy\Charlotte Trees\Charlotte Trees.gdb\CharMeanTemp",
    ignore_nodata="DATA",
    statistics_type="MEAN",
    process_as_multidimensional="CURRENT_SLICE",
    percentile_values=[90],
    percentile_interpolation_type="AUTO_DETECT",
    circular_calculation="ARITHMETIC",
    circular_wrap_value=360,
    out_join_layer=None
)

arcpy.analysis.SpatialJoin(
    target_features="Charlotte_Mecklenburg_Tree_Canopy",
    join_features="Zoning Join_Count",
    out_feature_class=r"C:\Users\lgtateos\Downloads\rawgraphs_data\Charlotte_Mecklenburg_Tree_Canopy\Charlotte Trees\Charlotte Trees.gdb\Charlotte_Meckle_SpatialJoin",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='TotalImp_1 "TotalImp_1" true true false 24 Double 0 0,First,#,Charlotte_Mecklenburg_Tree_Canopy,TotalImp_1,-1,-1;TotalTre_1 "TotalTre_1" true true false 24 Double 0 0,First,#,Charlotte_Mecklenburg_Tree_Canopy,TotalTre_1,-1,-1;Geography_ "Geography_" true true false 26 Text 0 0,First,#,Charlotte_Mecklenburg_Tree_Canopy,Geography_,0,25',
    match_option="LARGEST_OVERLAP",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)

arcpy.management.AddJoin(
    in_layer_or_view="Charlotte_Meckle_SpatialJoin",
    in_field="Geography_",
    join_table="CharMeanTemp",
    join_field="Geography_",
    join_type="KEEP_ALL",
    index_join_fields="NO_INDEX_JOIN_FIELDS",
    rebuild_index="NO_REBUILD_INDEX",
    join_operation="JOIN_ONE_TO_FIRST"
)

arcpy.conversion.ExportTable(
    in_table="Charlotte_Meckle_SpatialJoin",
    out_table=r"C:\Users\lgtateos\Downloads\rawgraphs_data\Charlotte_Mecklenburg_Tree_Canopy\Charlotte Trees\ChartlotteTreeCanopy_and_Temps.csv",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='Join_Count "Join_Count" true true false 4 Long 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.Join_Count,-1,-1;TARGET_FID "TARGET_FID" true true false 4 Long 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.TARGET_FID,-1,-1;TotalImp_1 "TotalImp_1" true true false 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.TotalImp_1,-1,-1;TotalTre_1 "TotalTre_1" true true false 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.TotalTre_1,-1,-1;Geography_ "Geography_" true true false 26 Text 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.Geography_,0,25;Shape_Length "Shape_Length" false true true 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,Charlotte_Meckle_SpatialJoin.Shape_Area,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.OBJECTID,-1,-1;Geography_ "Geography_" true true false 26 Text 0 0,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.Geography_,0,25;ZONE_CODE "ZONE_CODE" true true false 4 Long 0 0,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.ZONE_CODE,-1,-1;COUNT "COUNT" true true false 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.COUNT,-1,-1;AREA "AREA" true true false 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.AREA,-1,-1;MEAN "MEAN" true true false 8 Double 0 0,First,#,Charlotte_Meckle_SpatialJoin,CharMeanTemp.MEAN,-1,-1',
    sort_field=None
)