FROM RRKKKS/xxx:slim-buster

RUN git clone https://github.com/RRKKKS/xxx.git /root/IqArab
WORKDIR /root/IqArab

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/IqArab/bin:$PATH"

CMD ["python3","-m","IqArab"]
