def clean_text_file(input_file, output_file):
    try:
        with open(input_file, 'r')as infile:
            lines=infile.readlines()

            cleanded_lines=[line.strip() for line in lines]
            cleanded_lines.sort()

        with open(output_file, 'w')as outputfile:
            for line in cleanded_lines:
                outputfile.write(line+'\n')

        print(f"정리 완료 결과가 {output_file}에 저장되었습니다.")

    except FileNotFoundError:
            print(f"파일 {input_file}을 찾을수가 없습니다.")
    except Exception as e:
            print(f"에러 발생:{e}")


if __name__ == "__main__":
    input_path="input.txt"
    output_path = "output.txt"
    clean_text_file(input_path, output_path)
