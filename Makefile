all: q1 q3 q4 q5

clean:
	rm fail.fastq
	rm pass.fastq
	rm readlengths.txt

pass.fastq: downloads/pass
	poretools fastq --type 2D downloads/pass/ > pass.fastq

fail.fastq: downloads/fail
	poretools fastq --type 2D downloads/fail/ > fail.fastq

q1: pass.fastq fail.fastq
	python group2_report1_question1.py pass.fastq fail.fastq

q2: downloads/pass downloads/fail
	python group2_report1_question2.py downloads/

q3: downloads/pass downloads/fail
	python group2_report1_question3.py downloads/

q4: downloads/pass downloads/fail
	python group2_report1_question4.py downloads/

q5: downloads/pass downloads/fail
	python group2_report1_question5.py ./
