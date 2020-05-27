# (team72, Dongfang, Wang, 906257)
from matplotlib.path import Path
import numpy as np
import geopandas as gpd
import dbfread as dbr

NSW_map = gpd.read_file('NSW_LGA_POLYGON_shp.shp')
NSW_name_table1 = dbr.DBF('NSW_LGA_POLYGON_shp.dbf')
NSW_name_table2 = dbr.DBF('NSW_LGA_shp.dbf')

NT_map = gpd.read_file('NT_LGA_POLYGON_shp.shp')
NT_name_table1 = dbr.DBF('NT_LGA_POLYGON_shp.dbf')
NT_name_table2 = dbr.DBF('NT_LGA_shp.dbf')

OT_map = gpd.read_file('OT_LGA_POLYGON_shp.shp')
OT_name_table1 = dbr.DBF('OT_LGA_POLYGON_shp.dbf')
OT_name_table2 = dbr.DBF('OT_LGA_shp.dbf')

QLD_map = gpd.read_file('QLD_LGA_POLYGON_shp.shp')
QLD_name_table1 = dbr.DBF('QLD_LGA_POLYGON_shp.dbf')
QLD_name_table2 = dbr.DBF('QLD_LGA_shp.dbf')

SA_map = gpd.read_file('SA_LGA_POLYGON_shp.shp')
SA_name_table1 = dbr.DBF('SA_LGA_POLYGON_shp.dbf')
SA_name_table2 = dbr.DBF('SA_LGA_shp.dbf')

TAS_map = gpd.read_file('TAS_LGA_POLYGON_shp.shp')
TAS_name_table1 = dbr.DBF('TAS_LGA_POLYGON_shp.dbf')
TAS_name_table2 = dbr.DBF('TAS_LGA_shp.dbf')

VIC_map = gpd.read_file('VIC_LGA_POLYGON_shp.shp')
VIC_name_table1 = dbr.DBF('VIC_LGA_POLYGON_shp.dbf')
VIC_name_table2 = dbr.DBF('VIC_LGA_shp.dbf')

WA_map = gpd.read_file('WA_LGA_POLYGON_shp.shp')
WA_name_table1 = dbr.DBF('WA_LGA_POLYGON_shp.dbf')
WA_name_table2 = dbr.DBF('WA_LGA_shp.dbf')

#input the coordinate
points = np.array([[144.957039, -37.818668], [144.965754, -37.803582], [130.843213, -12.429449], [180.723799, -100.885078],[151.191270,-33.896546]])
#points = np.array[[151.191270, -33.896546]]

#find name function
def find_name(point):
    flag = 0
    if flag == 0:
        for i in range(len(NSW_map.boundary)):
            try:
                region = Path(NSW_map.boundary[i])
                if region.contains_point(point):
                    #print('test1')
                    LG_PLY_PID = NSW_map['LG_PLY_PID'][i]
                    for record1 in NSW_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            #print('test2')
                            LGA_PID = record1['LGA_PID']
                            for record2 in NSW_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    #print('test3')
                                    #result = 'test4'
                                    result = 'NSW ' + record2['ABB_NAME']
                                    #print(record2['ABB_NAME'])
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue

    if flag == 0:
        for i in range(len(NT_map.boundary)):
            try:
                region = Path(NT_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = NT_map['LG_PLY_PID'][i]
                    for record1 in NT_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in NT_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'NT ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(OT_map.boundary)):
            try:
                region = Path(OT_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = OT_map['LG_PLY_PID'][i]
                    for record1 in OT_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in OT_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'OT ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(QLD_map.boundary)):
            try:
                region = Path(QLD_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = QLD_map['LG_PLY_PID'][i]
                    for record1 in QLD_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in QLD_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'QLD ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(SA_map.boundary)):
            try:
                region = Path(SA_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = SA_map['LG_PLY_PID'][i]
                    for record1 in SA_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in SA_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'SA ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(TAS_map.boundary)):
            try:
                region = Path(TAS_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = TAS_map['LG_PLY_PID'][i]
                    for record1 in TAS_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in TAS_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'TAS ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(VIC_map.boundary)):
            try:
                region = Path(VIC_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = VIC_map['LG_PLY_PID'][i]
                    for record1 in VIC_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in VIC_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'VIC ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
        for i in range(len(WA_map.boundary)):
            try:
                region = Path(WA_map.boundary[i])
                if region.contains_point(point):
                    LG_PLY_PID = WA_map['LG_PLY_PID'][i]
                    for record1 in WA_name_table1:
                        if LG_PLY_PID == record1['LG_PLY_PID']:
                            LGA_PID = record1['LGA_PID']
                            for record2 in WA_name_table2:
                                if LGA_PID == record2['LGA_PID']:
                                    result = 'WA ' + record2['LGA_NAME']
                                    flag = 1
                                    break
                            break
                    break
            except:
                continue
    if flag == 0:
            result = "Can't find this point"
    return result


#Output state name and city name.
for point in points:
    name = find_name(point)
    print(name)
