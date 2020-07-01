# MYCO Data Format

As MYCO is covering a myriad of climate data, we will need to ensure that the properties of each dataset is laid out so that when other people access our data, they can easily
understand what the dataset covers. For our contributors, please follow the following guidelines when you collect your data.

## Describing the data in the README.md for each folder

When you initiate a climate metric folder, please include the description of the data in the README.md file under "Data Format" using a h2 header. You can refer to the following
example when tabulating the description of your dataset:

| Variable Name | Variable Type | Description | Unit | Example |
| :-----------: | :-----------: | :---------: | :--: | :-----: |
| Location | `string` | Unique location of the data collection site | None | `"Cheras, Kuala Lumpur"` |
| Value | `float` | Recorded Value | `air pollution index` | `"14.2 "` |
| ...   |  ...  | ...   |  ...  | ... |

## What should be included in the data description

Ideally, we would like to include as much information about a particular dataset as possible so that it is easier to perform query on them. If you have any questions regarding
what should you keep in your dataset, give us a shoutout in our main communication channel and we will reach out to you.

## Metadata

Besides the tabulated variable descriptions, we would also need to ensure that we include other relevant data that will be helpful for others when they need to use the data.
Please include the following information in your README.md under "Metadata" using a h2 header：

* Purpose of the data
* Time period of creation
* Creator/author/publishing entity of the data
* Contributor of the data (you!)
* Detailed sources (links) of the data involved in the creation of the dataset
* Data usage and licensing declaration (links to original license)
* File size
* Briefly describe the data creation process

