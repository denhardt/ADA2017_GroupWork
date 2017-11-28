# Title
Do we really have the freedom to vote on what we want to?

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
Once we have wrangled the data into a useful format we will primarily be using
Latent Dirichlet Allocation (LDA) in order to cluster articles based on what sub-topics
they are made up of. Using this unsupervised learning algorithm we will be able to more
closely analyse the different topics into which the data is grouped into. For
example by looking into the distribution through time of a certain topic. This
can give insights into how the subject of votations has changed through time.
We may also perform LDA on a subset of the data which only includes articles
related to direct-democracy initiatives. Comparing the topics between this
subset and the entire set may also suggest how direct-democracy has been used
in the past.

# Dataset
The main dataset we want to use are the archives Le Temps. After talking with
Giovanni we understand that these will be available on the cluster in a
processed from, with the articles available as strings and images. Although
the archives are enormous, we will only be using the fraction of them that is
related to voting. The raw data mining part of this project will be related to
string handling and processing. As we will already have the articles available
in text form we won't have to do any extraction of data from the raw images.

In terms of data wrangling and formatting we will be merged all articles from
the set together while keeping information concerning publication dates. We
will then have to select articles which are directly related to voting, and those
which are about only direct-democracy initiatives. In order to produce better
data for LDA we will then select a neighbourhood of words in each article that
is close to mentions of voting. By lemmatising the remaining text we will further
strip out any conjugation, suffixes and prefixes and aid in comparison between
articles. Once all this is done, we may finally perform LDA on the result.

# A list of internal milestones up until project milestone 2
01. ~~Getting familiar with working on the cluster, accessing and manipulating
the datasets.~~
02. Filtering and sorting the dataset according to our central theme. **done**
03. String handling and processing. Coming up with different methods (possibly
  looking into potential ML algorithms) to sort and extract data. **mostly done**
04. Looking at votation topics throughout history, visualisation of these
topics throughout time.

# Questions for TAs
