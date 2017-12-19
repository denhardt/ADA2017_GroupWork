# Title
Evolution of Direct Democracy in Switzerland

# Abstract
Our project follows this central question about democracy in Switzerland.
Our primary data source for this are the archives of the Swiss newspaper 'Le Temps',
which regroups data from three different newspapers from the past 200 years.
We want to see what kind of patterns we can see that surround Swiss voting
themes of the past and the present. Are we continuously voting on the same questions?
Do our answers to these questions change? What about entirely new themes? In
the last 200 years, life in Switzerland has radically changed, we would expect
this to be reflected in the topics that have been voted on. Especially with
regards to technological development and social norms. How has the voting
process been used to bring in these new changes under Swiss law?
While the archives from 'Le Temps' will serve as our reference, we will try to
make a comparison with present day trends using the Swiss tweets dataset.

# Research questions
* Do we have the freedom to vote on any question we wish?
* Do the same votations, or topics, keep coming up? Is this throughout history
or during specific periods?
* Are the results of these repeated votations changing throughout time?
* Can we link big changes in technological and societal norms to previous votations?
* How has direct democracy been used? Is it increasing or decreasing? What kind
of votations is it used for?

# Dataset
The main dataset we want to use are the archives Le Temps. After talking with
Giovanni we understand that these will be available on the cluster in a
processed from, with the articles available as strings and images. Although
the archives are enormous, we will only be using the fraction of them that is
related to voting. The raw data mining part of this project will be related to
string handling and processing. As we will already have the articles available
in text form we won't have to do any extraction of data from the raw images.
We'll also need to learn how to work on the
cluster, including how we will be querying the archives and sorting through
them.

Our secondary dataset will be the collection of Swiss tweets. We'll also
be performing a lot of similar string handling and processing. There will
be additional processing of the metadata associated with these tweets,
primarily the geolocation of some of these tweets.
However, as the dataset is not yet available
we haven't been able to inspect its contents.

Both of these datasets are available
on the cluster, which should simplify the workflow.

# A list of internal milestones up until project milestone 2
01. ~~Getting familiar with working on the cluster, accessing and manipulating
the datasets.~~
02. ~~Filtering and sorting the dataset according to our central theme.~~
03. ~~String handling and processing. Coming up with different methods (possibly
  looking into potential ML algorithms) to sort and extract data.~~
04. ~~Looking at votation topics throughout history, visualisation of these
topics throughout time.~~

# Milestone3:

The notebook 'Milestone3' is better viewed with nbviewer:
[http://nbviewer.jupyter.org/github/robinde/ADA2017_GroupWork/blob/master/Project/Milestone%203.ipynb]



# Group member contributions
Pierre: Suggestion and implementation of LDA algorithm, initial implementation of data pipeline, implementation of
data handling, data reduction and data cleaning methods. Proposed an initial vizualisation. Writting up the report. Code comments.

Robin: Improvements to data pipeline. Performing all data reduction
and cleaning steps. Formatting all data into DataFrames. Data visualisation notebook.

Youssef: Work on LDA algotithm,Suggestion and implementation of the Naive Selection using keywords Data Selection and the implementation of data pipeline and Writing up the report.
