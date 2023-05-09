import komm
import files
from simulation import Simulation
from generator import create_data


sim = [ Simulation(komm.RepetitionCode(1), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.RepetitionCode(3), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.HammingCode(3), komm.BinarySymmetricChannel(0.01)),
        Simulation(komm.CyclicCode(length=2, generator_polynomial=0b11), komm.BinarySymmetricChannel(0.01)),    # CRC-1
        Simulation(komm.CyclicCode(length=15, generator_polynomial=0b10100110111), komm.BinarySymmetricChannel(0.01)), # BCH
       
        Simulation(komm.RepetitionCode(1), channels.GilbertModel(0.1, 0.01)),
        Simulation(komm.RepetitionCode(3), channels.GilbertModel(0.1, 0.01)),
        Simulation(komm.HammingCode(3), channels.GilbertModel(0.1, 0.01)),
        Simulation(komm.CyclicCode(length=2, generator_polynomial=0b11), channels.GilbertModel(0.1, 0.01)),  # CRC-1
        Simulation(komm.CyclicCode(length=15, generator_polynomial=0b10100110111), channels.GilbertModel(0.1, 0.01)),  # BCH
      ]


create_data("temp.txt")
msg = files.read_file("temp.txt")

with open("wyniki.csv", "w") as f:
        f.write("code;channel;msg_len;sent_len;errors;ber\n")
        for s in sim:
                a = s.send(msg)
                f.write(f"{s.code};{s.channel};{len(a[0])};{a[1]};{a[2]};{a[3]}\n")
