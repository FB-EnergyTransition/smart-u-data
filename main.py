import pandas as pd


def get_affdex_data():
    affdex_file = pd.read_csv("input_data/AFFDEX_Statistics.csv", header=4)
    study_name_column = affdex_file['Study Name'].tolist()
    respondent_name_column = affdex_file['Respondent Name'].tolist()
    gender_column = affdex_file['Gender'].tolist()
    age_column = affdex_file['Age'].tolist()
    group_column = affdex_file['Group'].tolist()
    type_column = affdex_file['Type'].tolist()
    label_column = affdex_file['Label'].tolist()
    start_column = affdex_file['Start (ms)'].tolist()
    duration_column = affdex_file['Duration (ms)'].tolist()
    parent_stimulus_column = affdex_file['Parent Stimulus'].tolist()
    count_frames_column = affdex_file['Count Frames'].tolist()
    anger_column = affdex_file['Anger Time Percentage'].tolist()
    sadness_column = affdex_file['Sadness Time Percentage'].tolist()
    disgust_column = affdex_file['Disgust Time Percentage'].tolist()
    joy_column = affdex_file['Joy Time Percentage'].tolist()
    surprise_column = affdex_file['Surprise Time Percentage'].tolist()
    fear_column = affdex_file['Fear Time Percentage'].tolist()
    contempt_column = affdex_file['Contempt Time Percentage'].tolist()
    engagement_column = affdex_file['Engagement Time Percentage'].tolist()
    attention_column = affdex_file['Attention Time Percentage'].tolist()
    positive_column = affdex_file['Positive Time Percentage'].tolist()
    negative_column = affdex_file['Negative Time Percentage'].tolist()
    neutral_column = affdex_file['Neutral Time Percentage'].tolist()
    brow_furrow_column = affdex_file['Brow Furrow Time Percentage'].tolist()
    smile_column = affdex_file['Smile Time Percentage'].tolist()
    sentimentality_column = affdex_file['Sentimentality Time Percentage'].tolist()
    confusion_column = affdex_file['Confusion Time Percentage'].tolist()

    return {"Study Name": study_name_column,
            "Respondent Name": respondent_name_column,
            "Gender": gender_column,
            "Age": age_column,
            "Group": group_column,
            "Type": type_column,
            "Label": label_column,
            "Start (ms)": start_column,
            "Duration (ms)": duration_column,
            "Parent Stimulus": parent_stimulus_column,
            "Count Frames": count_frames_column,
            "Anger Time Percentage": anger_column,
            "Sadness Time Percentage": sadness_column,
            "Disgust Time Percentage": disgust_column,
            "Joy Time Percentage": joy_column,
            "Surprise Time Percentage": surprise_column,
            "Fear Time Percentage": fear_column,
            "Contempt Time Percentage": contempt_column,
            "Engagement Time Percentage": engagement_column,
            "Attention Time Percentage": attention_column,
            "Positive Time Percentage": positive_column,
            "Negative Time Percentage": negative_column,
            "Neutral Time Percentage": neutral_column,
            "Brow Furrow Time Percentage": brow_furrow_column,
            "Smile Time Percentage": smile_column,
            "Sentimentality Time Percentage": sentimentality_column,
            "Confusion Time Percentage": confusion_column}


def get_gsr_data():
    gsr_file = pd.read_csv("input_data/GSRPeakMetrics.csv")


def create_output(affdex_dict):
    df = pd.DataFrame(data=affdex_dict)
    df.to_excel("output.xlsx", index=False)


if __name__ == '__main__':
    affdex_dict = get_affdex_data()
    create_output(affdex_dict)


