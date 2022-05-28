FROM pytorch/pytorch

RUN pip install scikit-learn==1.0.2 tqdm jupyter tqdm pandas pycaret-ts-alpha tsai

RUN mkdir /workfolder

COPY ./* /workfolder/
COPY ./train_ipnbs/* /workfolder/

CMD jupyter notebook --ip 0.0.0.0 --allow-root

WORKDIR /workfolder
