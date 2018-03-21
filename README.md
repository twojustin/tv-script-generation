# TV Script Generation (Udacity project)

a sample dataset is included in `data/` directory
full script data is avaiable at [kaggle](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data/data)




## Development:

### to run jupyter in `floydhub`:
```
floyd run --mode jupyter --gpu
floyd run \
  --data twojustin/datasets/the-simpsons-by-the-data/1:the-simpsons-by-the-data \
  --mode \
  jupyter --gpu
```

### download results back to local:
```
floyd data clone twojustin/projects/tv-script-generation/3/output
```
where `tv-script-generation/3` is the project/job

