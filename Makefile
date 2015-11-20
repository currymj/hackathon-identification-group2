all: q1 q2 q3 q4 q5

clean:
	rm fail.fastq
	rm pass.fastq
	rm Q2channeloutput.txt
	rm Q5readlengths.txt
	rm pass.tsv
	rm fail.tsv

pass.fastq: downloads/pass
	poretools fastq --type 2D downloads/pass/ > pass.fastq

fail.fastq: downloads/fail
	poretools fastq --type 2D downloads/fail/ > fail.fastq

pass.tsv: downloads/pass
		poretools tabular --type 2D downloads/pass > pass.tsv

fail.tsv: downloads/fail
		poretools tabular --type 2D downloads/fail > fail.tsv

q1: pass.fastq fail.fastq group2_report1_question1.py
	python group2_report1_question1.py pass.fastq fail.fastq

q2: downloads/pass downloads/fail group2_report1_question2.py
	python group2_report1_question2.py ./

q3: downloads/pass downloads/fail pass.tsv fail.tsv group2_report1_question3.py
	python group2_report1_question3.py ./

q4: downloads/pass downloads/fail group2_report1_question4.py
	python group2_report1_question4.py ./

q5: downloads/pass downloads/fail group2_report1_question5.py
	python group2_report1_question5.py ./
