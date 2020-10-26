# Malaysia's Roadmap towards Zero Single-Use Plastic 2018-2030

The Malaysia's Roadmap towards Zero Single-Use Plastic 2018-2030 ("Roadmap") is designed "to take a phased, evidence-based and holistic approach by involving all stakeholders
in jointly addressing single-use plastics pollution in Malaysia."
According to its publishing entity, Ministry of Energy, Science, Technology, Environment & Climate Change (MESTECC), the Roadmap "is envisaged to deploy actions 
that can deflect the current trajectory to a more sustainable pathway towards a cleaner and healthier environment by 2030."

This Roadmap will be implemented from 2018 leading up to 2030, assuming that all relevant stakeholders will play their roles effectively to support the objectives of this Roadmap. You can access to the data used for the analysis shared in this repository here ([corpus](https://www.dropbox.com/s/xtbbl1htsvlm6gy/MRZSUP-corpus.csv), [document-term matrix](https://www.dropbox.com/s/f0zkugvwse4f6d8/MRZSUP-dtm.csv)). 

## Data Format 
For the text corpus,

| Variable Name | Variable Type | Description | Unit | Example |
| :-----------: | :-----------: | :---------: | :--: | :-----: |
| Primary Key | `integer` | Document Page | None | `"12311"`|
| page_content | `string` | Content on each page of the policy document | None | `"by cleaner and healthier ..."`|

For the document-term matrix,

| Variable Name | Variable Type | Description | Unit | Example |
| :-----------: | :-----------: | :---------: | :--: | :-----: |
| Primary Key | `integer` | Document Page | None | `"12311"`|
| *Vocabulary* | `integer` | Dummy indicating if the vocabulary appeared in the particular page | None | `"1", "0"`|
| ... | `integer` | Dummy indicating if the vocabulary appeared in the particular page | None | `"1", "0"`|

## Meta Data

### Purpose

Conduct textual analysis on our national environmental policies. 

### Time Period of Creation

This dataset is cleaned and organized from July 2020 - October 2020.

### Contributor

@XD-Ooi

### Data Source

Published by the Ministry of Energy, Science, Technology, Environment & Climate Change (MESTECC) in 2018. The original PDF copy can be accessed 
[here](https://www.mestecc.gov.my/web/wp-content/uploads/2019/03/Malaysia-Roadmap-Towards-Zero-Single-Use-Plastics-2018-20302.pdf).

### Terms of Use

This publication may be reproduced in whole or in part and in any form for educational or non-profit purposes without special permission from the
Ministry of Energy, Science, Technology, Environment & Climate Change (MESTECC), provided acknowledgement of the source is made. MESTECC
would appreciate receiving a copy of any publication that uses this publication as a source. No use of this publication may be made for resale or for
any other commercial purpose whatsoever without prior permission in writing from MESTECC. 

