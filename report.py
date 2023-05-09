import os
import pandas as pd
import matplotlib.pyplot as plt

def generate_report(file_name: str):
    # Read the CSV file
    data = pd.read_csv(file_name, sep=';')

    # Create graphs directory
    images_directory = "graphs"
    if not os.path.exists(images_directory):
        os.makedirs(images_directory)

    # Group the data by code and channel and calculate the mean of each column
    grouped_data = data.groupby(['Code', 'Channel name']).mean()

    # Reset the index and create a new column that concatenates the Code and Channel name
    grouped_data = grouped_data.reset_index()
    grouped_data['Code & Channel'] = grouped_data['Code'] + ' ' + grouped_data['Channel name']

    # Create a bar chart for the message length and sent message length
    bar_width = 0.35
    r1 = range(len(grouped_data))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, grouped_data['Message length'], color='blue', width=bar_width, label='Message length')
    plt.bar(r2, grouped_data['Sent message length'], color='orange', width=bar_width, label='Sent message length')

    plt.title('Message Length vs Sent Message Length')
    plt.xlabel('Code, Channel')
    plt.ylabel('Length')
    plt.xticks([r + bar_width / 2 for r in range(len(grouped_data))], grouped_data['Code & Channel'], rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig('./data/message_length_vs_sent_message_length.png', bbox_inches='tight')
    plt.clf()

    # Create a bar chart for the number of errors
    plt.bar(grouped_data['Code & Channel'], grouped_data['Number of errors'], color='blue')
    plt.title('Number of Errors')
    plt.xlabel('Code, Channel')
    plt.ylabel('Number of Errors')
    plt.xticks(rotation=90)
    plt.savefig("./data/number_of_errors.png", bbox_inches='tight');
    plt.clf()

    # Create a bar chart for the bit error rate
    plt.bar(grouped_data['Code & Channel'], grouped_data['Bit error rate'], color='blue')
    plt.title('Bit Error Rate')
    plt.xlabel('Code, Channel')
    plt.ylabel('Rate')
    plt.xticks(rotation=90)
    plt.savefig("./data/bit_error_rate.png", bbox_inches='tight');
    plt.clf()