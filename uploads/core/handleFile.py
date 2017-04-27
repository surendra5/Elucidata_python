import pandas as pd


def process_file(file_handle):
    df = pd.read_csv('file_handle', delimiter='\t', usecols=['Sample', 'Cohort', 'Metabolite Name', 'Intensity'])
    df = df[df['Cohort'].str.contains("std")]
    df = df.groupby(['Cohort', 'Metabolite Name'])['Intensity'].sum().reset_index()
    df = df[['Cohort', 'Intensity']]
    c = 'Cohort'
    s = df.set_index([c, df.groupby(c).cumcount() + 2]).Intensity
    df = s.unstack().add_prefix('Intensity').reset_index()
    return df.to_csv()