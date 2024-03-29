import csv

statsFile = open("statsFile.csv")
statReader = csv.reader(statsFile)
newStats = open("reformatted.csv", "w+")

csv_header = "name, season, type, stat"
newStats.write(csv_header + "\n")

header = "season,age,team_id,lg_id,pos,g,gs,mp_per_g,fg_per_g,fga_per_g,fg_pct,fg3_per_g,fg3a_per_g,fg3_pct,fg2_per_g,fg2a_per_g,fg2_pct,efg_pct,ft_per_g,fta_per_g,ft_pct,orb_per_g,drb_per_g,trb_per_g,ast_per_g,stl_per_g,blk_per_g,tov_per_g,pf_per_g,pts_per_g,mp,per,ts_pct,fg3a_per_fga_pct,fta_per_fga_pct,orb_pct,drb_pct,trb_pct,ast_pct,stl_pct,blk_pct,tov_pct,usg_pct,ws-dum,ows,dws,ws,ws_per_48,bpm-dum,obpm,dbpm,bpm,vorp,name"
labels = header.split(",")

count = 0

for row in statReader:
    if count == 0:
        count += 1
        continue

    name = row[len(row) - 1]
    season = row[0]

    for i in range(len(row)):
        if labels[i] in ["season", "name"]:
            continue
        data = name + ", " + season + ", " + labels[i] + ", " + row[i]
        newStats.write(data + "\n")
    
    count += 1

newStats.close()
statsFile.close()