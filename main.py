import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default= "plotly_white"

data = pd.read_csv("Sample - Superstore.csv", encoding = 'latin-1')
data.head()

data.info()

#Converting date columns
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])

data.info()

data['Order Month']= data['Order Date'].dt.month
data['Order Year']= data['Order Date'].dt.year
data['Order weekday']= data['Order Date'].dt.dayofweek

data.head()

#Monthly Sales Analysis
sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
fig=px.line(sales_by_month, x='Order Month',y='Sales', title='Monthly Sales Analysis')

sales_by_month
fig.show()

#Sales by category
sales_by_category= data.groupby('Category')['Sales'].sum().reset_index()
sales_by_category

fig=px.pie(sales_by_category, values='Sales', names='Category', color_discrete_sequence= px.colors.qualitative.Pastel)
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.update_layout(title_text='Sales Analysis by category', title_font=dict(size=24))

fig.show()

# Sales Analysis by Sub-category
sale_by_subcategory= data.groupby('Sub-Category')['Sales'].sum().reset_index()
sale_by_subcategory

fig=px.bar(sale_by_subcategory, x='Sub-Category', y='Sales', title="Sales by Sub-Category")
fig.show()

#Monthly Profit Analysis
profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()
profit_by_month

fig=px.bar(profit_by_month, x='Order Month', y='Profit', title='Monthly Analysis')
fig.show()

#Profit by Category
profit_by_category= data.groupby('Category')['Profit'].sum().reset_index()
profit_by_category

fig = px.pie(profit_by_category, values='Profit', names='Category', color_discrete_sequence= px.colors.qualitative.Pastel)
fig.update_traces(textposition = 'inside', textinfo = 'percent+label')
fig.update_layout(title_text='Profit Analysis by category', title_font=dict(size=24))

fig.show()

profit_by_subcategory= data.groupby('Sub-Category')['Profit'].sum().reset_index()
profit_by_subcategory

fig=px.bar(profit_by_subcategory, x='Sub-Category', y='Profit', title='Profit Analysis by Sub category')
fig.show()

#Sales and Profit - Customer Segment
Customer_segment= data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
Customer_segment

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=Customer_segment['Segment'],
                     y=Customer_segment['Sales'], 
                     name='Sales',
                     marker_color= color_palette[0]))

fig.add_trace(go.Bar(x=Customer_segment['Segment'],
                     y=Customer_segment['Profit'],
                     name='Profit',
                     marker_color= color_palette[1]))

fig.update_layout(title ='Sales and Profit Analysis - Customer Segment',
                  xaxis_title='Customer Segment',
                  yaxis_title='Amount')

fig.show()


#Sales and Profit Ratio
Customer_segment= data.groupby('Segment').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
Customer_segment['Sales_to_profit_ratio'] = Customer_segment['Sales'] / Customer_segment['Profit']
print(Customer_segment[['Segment','Sales_to_profit_ratio']])

