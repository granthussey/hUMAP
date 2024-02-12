# hUMAP

**Visualize structure in large microbiome datasets. Implements Uniform Manifold Approximation and Projection (UMAP) with hierarchy.**

## Installation


## 
```
git clone https://github.com/granthussey/humap.git
pip install -e humap
```

## Usage

### Command line:

```bash
python run_humap.py -t hierarchy.csv -m data.csv -n 15
```
Your embedding will be saved in the `humap/results/` folder. 


### Python:
```python
from humap.humap import Humap

##### Initialize hUMAP object #####

# From file
h = Humap(hierarchy='path/to/hierarchy.csv', 
        data='path/to/data.csv')

# OR #

# From local variable scope
h = Humap(hierarchy=df_hierarchy, 
        data=df)


##### Run the transformation and look at the results #####

# Transform the data (an inplace function)
h.transform_self(neigh=13)

# Raw embedding dataframe
h.df_embedding

# "Which taxon dominate each sample?" dataframe
h.df_dominant_level

# Visualize the embedding
h.scatter()

# Save the embedding
h.save_embedding() 

```
---

## Flags for `run_taxumap.py`

### Required

* `-t` or `--taxonomy`: filepath to your `taxonomy.csv` file
* `-m` or `--microbiota`: filepath to your `microbiota_table.csv` file
* `-n` or `--neigh`: number of patients

### Optional, but recommended

* `-a` or `--agg_levels`: Which taxonomic levels to aggregate, in the form of a `/`-delimined string (e.g. `Phylum/Family`)
* `-w` or `--weights`: Weights to give to each taxonomic level defined in `--agg_levels`, in the form of a `/`-delimined string (e.g. `5/6`, `0.5/2`, `6/2/1`, etc). Defaults to 1 for each.
* 

### Optional, change default behavior

* `-o` or `--outdir`: Where to save embedding. Defaults to `phylo-umap/results`.
* `-v` or `--verbose`: Add flag to log INFO-level information.
* `-d` or `--debug`: Add flag to log DEBUG-level information.
* `-s` or `--save`: Set to False to not save the embedding. Defaults to True.
* `-b` or `--min_dist`: Change the `min_dist` parameter passed to the UMAP algorithm. See documentation [here](https://umap-learn.readthedocs.io/en/latest/parameters.html?highlight=min_dist#min-dist). 


## Documentation for Taxumap as a Package

See this link. (In progress)

---

## Details
Two tables are required: the data table and a hierarchy table.

The ***data file*** (`data.csv`) must have a column with sample indices labeled 'index_column'. The remaining columns are expected to be the lowest level hierarchy (e.g., OTU/ASV/... for microbiome data):

| index_column | ASV1 | ASV2 |
| :--- | :---: | :---: |
|'sample1'| 0.5| 0.5|
|'sample2'|0.2| 0.8|


The ***hierarchy table*** (`hierachy.csv`) is expected to resolve higher hierarchical groups for the columns in the data table. The columns of this table should contain hierarchical levels. They should be ordered from left to right in decreasing hierarchy, e.g.

| kingdom    | phylum       | ...   | ASV    |
| :---       | :---:        | :---: | :---:  |
| 'Bacteria' | 'Firmicutes' | ...   | 'ASV1' |

Unless designated by the `-t` and `-m` flags, the data is expected to be within the `data/` folder. Results are written to the `humap/results/` folder.

---

## Roadmap

---

## Example data

A dataset provided by Axel Olin works well for those wanting to try out the features of hUMAP or to better understand how to format your own data properly.

* [Link to original publication](https://pubmed.ncbi.nlm.nih.gov/30142345/)
* [Link to the dataset](http://dx.doi.org/10.17632/ynhdrcxtcc.1)

Publication
> Olin A, Henckel E, Chen Y, et al. Stereotypic Immune System Development in Newborn Children. Cell. 2018;174(5):1277-1292.e14. doi:10.1016/j.cell.2018.06.045

Dataset
> Olin, Axel (2018), “Stereotypic Immune System Development in Newborn Children”, Mendeley Data, v1


## License

[MIT](https://choosealicense.com/licenses/mit/)