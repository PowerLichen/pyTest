"""
  Project: Homework 8.4
  Author: 최민수
  StudentID: 21511796
  Date of last update: May. 3, 2021
  Detail: myMtrx로 생성된 mA를 pickle,json 파일로 저장하고 size를 출력
"""
import CustomJsonEncoder
import os
import test_myClassMtrx
import json
import pickle

def main():
    # prepare mA, mB
    # operations for mC, mD, mE
    #‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
    # Comparison of storage of mA in JSON text file and pickle bin file
    f_json = open("mA_json.txt", "w")
    json.dump(mA, f_json, indent=4, cls=CustomJsonEncoder.CustomEncoder)
    f_json.close()

    size_f_json = os.path.getsize("mA_json.txt")
    print("size of mA_json.txt = ", size_f_json)
    f_pickle = open("mA_pickle.bin", "wb")
    pickle.dump(mA, f_pickle)
    f_pickle.close()

    size_f_pickle = os.path.getsize("mA_pickle.bin")
    print("size of mA_pickle.bin = ", size_f_pickle)

if __name__ == "__main__":
    print("Executing main()")
    with open('matrix_data.txt') as f:
        mA = test_myClassMtrx.setMtrx(f, "mA")
    main()