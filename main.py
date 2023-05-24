import komm
import files
import channels
from simulation import Simulation
from generator import create_data
from report import generate_report

simulations = [ Simulation(komm.RepetitionCode(1), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.RepetitionCode(3), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.HammingCode(3), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.CyclicCode(length=2, generator_polynomial=0b11), komm.BinarySymmetricChannel(0.01)),    # CRC-1
        Simulation(komm.CyclicCode(length=15, generator_polynomial=0b10100110111), komm.BinarySymmetricChannel(0.1)), # BCH
       
        Simulation(komm.RepetitionCode(1), channels.GilbertModel(0.001, 0.001)),
        Simulation(komm.RepetitionCode(3), channels.GilbertModel(0.001, 0.001)),
        Simulation(komm.HammingCode(3), channels.GilbertModel(0.001, 0.001)),
        Simulation(komm.CyclicCode(length=2, generator_polynomial=0b11), channels.GilbertModel(0.001, 0.001)),  # CRC-1
        Simulation(komm.CyclicCode(length=15, generator_polynomial=0b10100110111), channels.GilbertModel(0.001, 0.001)),  # BCH
      ]

temp_file_name = 'temp.txt'
create_data(temp_file_name)
message = files.read_file(temp_file_name)

results_file_name = 'results.csv'
with open(results_file_name, 'w') as file:
        file.write('Code;Channel name;Message length;Sent message length;Number of errors;Bit error rate\n')
        for simulation in simulations:
                simulation_result = simulation.send(message)
                file.write(f"{simulation.code};{simulation.channel};{len(simulation_result[0])};{simulation_result[1]};{simulation_result[2]};{simulation_result[3]}\n")

generate_report(results_file_name)