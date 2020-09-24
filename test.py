import pandas as pd
import matplotlib.pyplot as plt 
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.palettes import Spectral5,Spectral3,Inferno5,RdGy5
from bokeh.transform import factor_cmap

#The Basics of Bokeh
class bokeh_sketch_dots:

    def bokeh_sketch_dot_func(self):
        output_file('columndatasource_example.html')
        data=pd.read_csv("test.csv")
        #data.drop(["Hulu_id"],axis=1,inplace=True)
        print(data)
        p = figure()
        sample = data.sample(4)
        source = ColumnDataSource(sample)
        p.circle(x='TOTAL_TONS', y='AC_ATTACKING',
                 source=source,
                 size=10, color='green')

        p.title.text = 'Attacking Aircraft and Munitions Dropped'
        p.xaxis.axis_label = 'Tons of Munitions Dropped'
        p.yaxis.axis_label = 'Number of Attacking Aircraft'

        hover = HoverTool()
        hover.tooltips=[
            ('Attack Date', '@MSNDATE'),
            ('Attacking Aircraft', '@AC_ATTACKING'),
            ('Tons of Munitions', '@TOTAL_TONS'),
            ('Type of Aircraft', '@AIRCRAFT_NAME')
        ]

        p.add_tools(hover)

        show(p)

#Categorical Data and Bar Charts: Munitions Dropped by Country
class Bar_charts:
    """We also make two new imports: Spectral5 is a pre-made five color pallette,
    one of Bokehs many pre-made color palettes, and factor_cmap is a helper
    method for mapping colors to bars in a bar-charts."""
    def bar_charts(self):
        output_file('munitions_by_country.html')
        data = pd.read_csv('test.csv')
        # We now need to get from the 170,000+ 
        # records of individual missions to one record per attacking country with the total munitions dropped
        grouped = data.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG'].sum()
        """Pandas lets us do this in a single line of code by using the groupby dataframe method. 
        This method accepts a column by which to group the data and one or more aggregating methods 
        that tell Pandas how to group the data together. The output is a new dataframe.

        Let's take this one piece at a time. The groupby('COUNTRY_FLYING_MISSION') sets the column that
        we are grouping on. In other words, this says that we want the resulting dataframe to have one 
        row per unique entry in the column COUNTRY_FLYING_MISSION. Since we don't care about aggregating
        all 19 columns in the dataframe, we choose just the tons of munitions columns with the indexer,
        ['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG']. Finally, we use the sum method to let Pandas 
        know how to aggregate all of the different rows. Other methods also exist for aggregating, such 
        as count, mean, max, and min."""
        print(grouped)
        #To plot this data, let's convert to kilotons by dividing by 1000.

        grouped = grouped / 1000
        source = ColumnDataSource(grouped)
        countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
        p = figure(x_range=countries)
        """Now, we need to make a ColumnDataSource from our grouped data and create a figure.
        Since our x-axis will list the five countries (rather than numerical data) we need to 
        tell the figure how to handle the x-axis.
        To do this, we create a list of countries from our source object, using source.data 
        and the column name as key. The list of countries is then passed as the x_range to 
        our figure constructor. Because this is a list of text data, the figure knows the 
        x-axis is categorical and it also knows what possible values our x range can take 
        (i.e. AUSTRALIA, GREAT BRITAIN, etc.)."""

        color_map = factor_cmap(field_name='COUNTRY_FLYING_MISSION',
                            palette=Spectral5, factors=countries)

        p.vbar(x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', source=source, width=0.70, color=color_map)

        p.title.text ='Munitions Dropped by Allied Country'
        p.xaxis.axis_label = 'Country'
        p.yaxis.axis_label = 'Kilotons of Munitions'
        """To color our bars we use the factor_cmap helper function. This creates a special color
        map that matches an individual color to each category (i.e. what Bokeh calls a factor).
        The color map is then passed as the color argument to our vbar glyph method.
        For the data in our glyph method, passing a source and again referencing column 
        names. Instead of using a y parameter, however, the vbar method takes a top parameter.
        A bottom parameter can equally be specified, but if left out, its default value is 0."""

        hover = HoverTool()
        hover.tooltips = [
            ("Totals", "@TONS_HE High Explosive / @TONS_IC Incendiary / @TONS_FRAG Fragmentation")]
        hover.mode = 'vline'
        """ vline and hline tell the popup to show when a vertical or horizontal line crosses a glyph.
        With vline set here, anytime your mouse passes through an imaginary vertical line extending
        from each bar, a popup will show."""
        p.add_tools(hover)
        show(p)

#Stacked Bar Charts and Sub-sampling Data: Types of Munitions Dropped by Country
class stacked_Bar_charts:

    def stacked_bar_charts(self):
        #import pdb;pdb.set_trace()
        output_file('types_of_munitions.html')
        data = pd.read_csv('test.csv')
        filter = data['COUNTRY_FLYING_MISSION'].isin(('USA','GREAT BRITAIN'))
        data = data[filter] 
        grouped = data.groupby('COUNTRY_FLYING_MISSION')['TONS_IC', 'TONS_FRAG', 'TONS_HE'].sum()
        #convert tons to kilotons again
        grouped = grouped / 1000
        source = ColumnDataSource(grouped)
        countries = source.data['COUNTRY_FLYING_MISSION'].tolist()
        p = figure(x_range=countries)
        p.vbar_stack(stackers=['TONS_HE', 'TONS_FRAG', 'TONS_IC'],
                     x='COUNTRY_FLYING_MISSION', source=source,
                     legend = ['High Explosive', 'Fragmentation', 'Incendiary'],
                     width=0.5, color=Spectral3)
        """To create the stacked bar chart, we call the vbar_stack glyph method.
        Rather than passing a single column name to a y parameter, we instead pass
        a list of column names as stackers. The order of this list determines the 
        order that the columns will be stacked from bottom to top (after you've
        worked through this example, try switching the column order to see what happens).
        The legend argument supplies text for each stacker """
        p.title.text ='Types of Munitions Dropped by Allied Country'
        p.legend.location = 'top_left'
        p.xaxis.axis_label = 'Country'
        p.xgrid.grid_line_color = None  #remove the x grid lines
        p.yaxis.axis_label = 'Kilotons of Munitions'
        show(p)

#Time-Series and Annotations: Bombing Operations over Time-Series
class timeseries_annotations:

    def timeSeries_annotations(self):
        output_file('simple_timeseries_plot.html')

        df = pd.read_csv('test.csv')

        #make sure MSNDATE is a datetime format
        df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')

        grouped = df.groupby('MSNDATE')['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
        grouped = grouped/1000

        source = ColumnDataSource(grouped)

        p = figure(x_axis_type='datetime')

        p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=source, legend='All Munitions')
        p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=source, color=Spectral3[1], legend='Fragmentation')
        p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=source, color=Spectral3[2], legend='Incendiary')

        p.yaxis.axis_label = 'Kilotons of Munitions Dropped'

        show(p)

#Different Types of Charts for Analyzing & Presenting Data

#Histogram
class histogram_charts:

    def histogram_func(self):
        # create 2D array of table given above 
        data = [['E001', 'M', 34, 123, 'Normal', 350], 
                ['E002', 'F', 40, 114, 'Overweight', 450], 
                ['E003', 'F', 37, 135, 'Obesity', 169], 
                ['E004', 'M', 30, 139, 'Underweight', 189], 
                ['E005', 'F', 44, 117, 'Underweight', 183], 
                ['E006', 'M', 36, 121, 'Normal', 80], 
                ['E007', 'M', 32, 133, 'Obesity', 166], 
                ['E008', 'F', 26, 140, 'Normal', 120], 
                ['E009', 'M', 32, 133, 'Normal', 75], 
                ['E010', 'M', 36, 133, 'Underweight', 40] ] 
          
        # dataframe created with 
        # the above data array 
        data_array=pd.DataFrame(data,columns=['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'])
        data_array.hist()
        plt.show()

if __name__=="__main__":
    #bokeh_sketch_dots().bokeh_sketch_dot_func()
    #Bar_charts().bar_charts()
    #stacked_Bar_charts().stacked_bar_charts()
    #timeseries_annotations().timeSeries_annotations()
    histogram_charts().histogram_func()