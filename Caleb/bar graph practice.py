import plotly
plotly.tools.set_credentials_file(username='crhodes21', api_key='U4jIV8iTZLBAOUo9i3U1')

import plotly.plotly as py
import plotly.graph_objs as go

data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.iplot(data, filename='basic-bar')
