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
	python q1.py pass.fastq fail.fastq

q3: downloads/pass downloads/fail
	python q3.py downloads/

q4: downloads/pass downloads/fail
	python q4.py downloads/

q5: downloads/pass downloads/fail
	python q5.py ./
