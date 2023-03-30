import argparse

import pandas as pd
import numpy as np


def process_cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-affdex_file', type=str, default='AFFDEX_Statistics.csv',
                        help="Name of the file that contains the AFFDEX Statistics")
    parser.add_argument('-gsr_file', type=str, default='GSRPeakMetrics.csv',
                        help="Name of the file that contains the GSR Statistics")
    args = parser.parse_args()
    return args


def get_affdex_data(affdex_file):
    affdex = pd.read_csv(affdex_file, header=4)

    study_name_column = affdex['Study Name'].tolist()
    respondent_name_column = affdex['Respondent Name'].tolist()
    gender_column = affdex['Gender'].tolist()
    age_column = affdex['Age'].tolist()
    group_column = affdex['Group'].tolist()
    type_column = affdex['Type'].tolist()
    label_column = affdex['Label'].tolist()
    start_column = affdex['Start (ms)'].tolist()
    duration_column = affdex['Duration (ms)'].tolist()
    parent_stimulus_column = affdex['Parent Stimulus'].tolist()
    count_frames_column = affdex['Count Frames'].tolist()
    anger_column = affdex['Anger Time Percentage'].tolist()
    sadness_column = affdex['Sadness Time Percentage'].tolist()
    disgust_column = affdex['Disgust Time Percentage'].tolist()
    joy_column = affdex['Joy Time Percentage'].tolist()
    surprise_column = affdex['Surprise Time Percentage'].tolist()
    fear_column = affdex['Fear Time Percentage'].tolist()
    contempt_column = affdex['Contempt Time Percentage'].tolist()
    engagement_column = affdex['Engagement Time Percentage'].tolist()
    attention_column = affdex['Attention Time Percentage'].tolist()
    positive_column = affdex['Positive Time Percentage'].tolist()
    negative_column = affdex['Negative Time Percentage'].tolist()
    neutral_column = affdex['Neutral Time Percentage'].tolist()
    brow_furrow_column = affdex['Brow Furrow Time Percentage'].tolist()
    smile_column = affdex['Smile Time Percentage'].tolist()
    sentimentality_column = affdex['Sentimentality Time Percentage'].tolist()
    confusion_column = affdex['Confusion Time Percentage'].tolist()

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
            "Confusion Time Percentage": confusion_column
            }


def get_gsr_data(gsr_file):

    gsr = pd.read_csv(gsr_file, header=10)

    # stimmt! mit anderen Werten auch machen
    signal_duration = gsr.loc[:, ['Signal Duration', 'Signal Duration.1', 'Signal Duration.2', 'Signal Duration.3',
                                       'Signal Duration.4', 'Signal Duration.5', 'Signal Duration.6', 'Signal Duration.7',
                                       'Signal Duration.8']].mean(axis=1)
    #print(signal_duration)

    has_peaks = gsr.loc[:, ['Has Peaks', 'Has Peaks.1', 'Has Peaks.2', 'Has Peaks.3',
                                       'Has Peaks.4', 'Has Peaks.5', 'Has Peaks.6',
                                       'Has Peaks.7',
                                       'Has Peaks.8']].mean(axis=1)
    #print(has_peaks)

    peak_count = gsr.loc[:, ['Peak Count', 'Peak Count.1', 'Peak Count.2', 'Peak Count.3',
                                       'Peak Count.4', 'Peak Count.5', 'Peak Count.6',
                                       'Peak Count.7',
                                       'Peak Count.8']].mean(axis=1)

    peaks_per_minute = gsr.loc[:, ['Peaks Per Minute', 'Peaks Per Minute.1', 'Peaks Per Minute.2', 'Peaks Per Minute.3',
                                       'Peaks Per Minute.4', 'Peaks Per Minute.5', 'Peaks Per Minute.6',
                                       'Peaks Per Minute.7',
                                       'Peaks Per Minute.8']].mean(axis=1)

    average_peak_amplitude = gsr.loc[:, ['Average Peak Amplitude', 'Average Peak Amplitude.1', 'Average Peak Amplitude.2', 'Average Peak Amplitude.3',
                                       'Average Peak Amplitude.4', 'Average Peak Amplitude.5', 'Average Peak Amplitude.6',
                                       'Average Peak Amplitude.7',
                                       'Average Peak Amplitude.8']].mean(axis=1)

    respondent_name_column = gsr['Respondent Name'].tolist()

    return {"Respondent Name": respondent_name_column,
            "Signal Duration": signal_duration.tolist(),
            "Has Peaks": has_peaks.tolist(),
            "Peak Count": peak_count.tolist(),
            "Peaks Per Minute": peaks_per_minute.tolist(),
            "Average Peak Amplitude": average_peak_amplitude.tolist()
            }


def create_output(affdex_dict, gsr_dict):

    affdex_dict.update(gsr_dict)
    #for key in affdex_dict:
        #print(len(affdex_dict[key]))
    df = pd.DataFrame(data=affdex_dict)
    df.to_excel("output.xlsx", index=False)


def check_completeness(affdex_dict, gsr_dict):
    resp_affex = affdex_dict["Respondent Name"]
    resp_gsr = gsr_dict["Respondent Name"]

    for i in range(0, len(resp_affex)):
        if resp_affex[i] != resp_gsr[i]:

            count = resp_affex.count(resp_affex[i])
            for j in range(0, count):
                resp_gsr.insert(i+j, resp_affex[i])
                gsr_dict["Signal Duration"].insert(i+j, np.nan)
                gsr_dict["Has Peaks"].insert(i+j, np.nan)
                gsr_dict["Peak Count"].insert(i+j, np.nan)
                gsr_dict["Peaks Per Minute"].insert(i+j, np.nan)
                gsr_dict["Average Peak Amplitude"].insert(i+j, np.nan)
            break





if __name__ == '__main__':
    args = process_cli_arguments()
    print("AFFDEX file: " + args.affdex_file)
    print("GSR file: " + args.gsr_file)
    affdex_dict = get_affdex_data(args.affdex_file)
    gsr_dict = get_gsr_data(args.gsr_file)
    check_completeness(affdex_dict, gsr_dict)
    create_output(affdex_dict, gsr_dict)


