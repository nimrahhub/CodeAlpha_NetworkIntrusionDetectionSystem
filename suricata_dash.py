import json
from collections import Counter
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

LOG_FILE = "/var/log/suricata/eve.json"

def load_alerts():
alerts = []

```
try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("event_type") == "alert":
                    alerts.append(data)
            except:
                continue
except FileNotFoundError:
    pass

return alerts
```

def process_alerts(alerts):
ips = []

```
for alert in alerts:
    src_ip = alert.get("src_ip")
    if src_ip:
        ips.append(src_ip)

return Counter(ips)
```

app = Dash(**name**)

app.layout = html.Div([
html.H2("Network Intrusion Detection System Dashboard"),
html.P("Real-time attack monitoring using Suricata logs"),

```
dcc.Interval(id="interval", interval=5000, n_intervals=0),

dcc.Graph(id="attack-graph")
```

])

@app.callback(
Output("attack-graph", "figure"),
Input("interval", "n_intervals")
)
def update_graph(n):
alerts = load_alerts()
data = process_alerts(alerts)

```
if not data:
    fig = px.bar(
        x=["No Data"],
        y=[0],
        title="No Attacks Detected Yet"
    )
    return fig

fig = px.bar(
    x=list(data.keys()),
    y=list(data.values()),
    labels={"x": "Source IP", "y": "Attack Count"},
    title="Live Network Attack Visualization"
)

return fig
```

if **name** == "**main**":
app.run(debug=True, host="0.0.0.0", port=8050)
