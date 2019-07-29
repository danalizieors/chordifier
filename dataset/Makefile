LINK=https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.0.10.tar.xz

all: download extract process generate clean

download:
	curl -o kernel.tar.xz ${LINK}

extract:
	mkdir kernel
	tar xf kernel.tar.xz -C kernel --strip-components 1

process:
	find kernel -type f -exec cat {} + \
	| awk '{$$1=$$1};1' \
	> source.dat

generate:
	 export PYTHONPATH=.. && \
	 pipenv run python generate_ngram.py

clean:
	rm -rf kernel.tar.xz kernel source.dat
