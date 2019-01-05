import pandas as pd
df = pd.read_csv('agent_state_3rd_week.csv', index_col = 'Date')


#  here creating a new column from an existing one
df['state'] = df.StateType.str[:-7]

df = df[[ 'AgentName','StartTime', 'EndTime','StateType','State', 'Duration','ReleaseCode']]

polish = ['Evelina Szweda',  'Ferenc Kobzos' ,'Jakub Dymek', 'Katarzyna Swoboda', 'Magda Szast',
          'Sebastian Deszcz', 'Mirko Badyoczek', 'Tomasz Heffler', 'Malgorzata Rohnka']

#getting the agent names for checking truth  values and iteraion 
agentnames = df.AgentName.unique()
dates = list(df.index.unique())

# Write HTML String to file.html
with open("file.txt", "w") as file:
    file.write(str(dates))
#print(dates)
    a_d = {}

    for date in dates :
        new_df = df.loc[date]
        agents = list(new_df.AgentName.unique())
        file.write('\ndate:')
        file.write(date)
        d = {}
        for name in polish:
            file.write('\nagent name: ')
            file.write(name)
            if name in agents:
                b = {}
                file.write('worked')
                agent_df = new_df[new_df['AgentName']== name]
                agent_df = agent_df[['StartTime','EndTime','State','Duration', 'ReleaseCode']]
                file.write(str(agent_df.head()))
                file.write(str(agent_df.tail()))
                short = agent_df[agent_df['ReleaseCode']=='Short Break']
                #print('\nSHORT BREAKS')
                file.write(str(short.head(10)))
                sh = short.Duration.unique()
                shorts=[]
                for item in sh:
                    x= item.split(':')
                    shorts.append(x)
                result = []
                for item in shorts:
                    x = int(item[0])*60*60 + int(item[1])*60 + int(item[2])
                    result.append(x)
                #print('\ntotal time spent in short break:')
                #print(sum(result)/60)
                b['Short Break'] = round(sum(result)/60,2)
                lunch = agent_df[agent_df['ReleaseCode']=='Lunch Break']
                #print('\nLUNCH BREAKS')
                file.write(str(lunch.head(2)))
                ln = lunch.Duration.unique()
                lunchs=[]
                for item in ln:
                    c= item.split(':')
                    lunchs.append(c)
                result_l = []
                for item in lunchs:
                    k = int(item[0])*60*60 + int(item[1])*60 + int(item[2])
                    result_l.append(k)
                #print('\ntotal time spent in lunch break:')
                #print(sum(result_l)/60)
                b['Lunch Break'] = round(sum(result_l)/60, 2)
                outbound = agent_df[agent_df['ReleaseCode']=='Outbound']
                #print('\nOutbound')
                file.write(str(outbound.head(10)))
                ou = outbound.Duration.unique()
                outbounds=[]
                for item in ou:
                    c= item.split(':')
                    outbounds.append(c)
                result_o = []
                for item in outbounds:
                    k = int(item[0])*60*60 + int(item[1])*60 + int(item[2])
                    result_o.append(k)
                #print('\ntotal time spent in outbound:')
                b['outbound'] = round(sum(result_o)/60,2)
                #print(sum(result_o)/60)
                avail = agent_df[agent_df['State']=='Available']
                #print('\nAvailable')
                av = avail.Duration.unique()
                avails=[]
                for item in av:
                    c= item.split(':')
                    avails.append(c)
                result_a = []
                for item in avails:
                    k = int(item[0])*60*60 + int(item[1])*60 + int(item[2])
                    result_a.append(k)
                #print('\ntotal time spent in available:')
                b['available'] = round(sum(result_a)/60/60,2)
                #print(sum(result_a)/60/60)
                #print(b)
                in_call = agent_df[agent_df['State']== 'Available In Call']
                call = in_call.Duration.unique()
                calls= []
                for item in call:
                    c=item.split(':')
                    calls.append(c)
                result_c = []
                for item in calls:
                    k = int(item[0])*60*60 + int(item[1])*60 + int(item[2])
                    result_c.append(k)
                b['in call'] = round(sum(result_c)/60/60,2)
                
                d[name] = b
                
            else:
                file.write('nope did not work')

## TO-DO:
# Make HTML file: most probably using BeautifulSoup library







