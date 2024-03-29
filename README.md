# topic-controllable-summarization
Code for topic-controllable summarization

This repository contains code for paper: Topic-Aware Evaluation and Transformer Methods for Topic-Controllable Summarization

## Requirements

`datasets==1.0.1`\
`nltk==3.5`\
`numpy==1.19.2`\
`pandas==1.1.3`\
`torch==1.8.1`\
`transformers==4.11.0`

## Topic Embeddings 

To fine-tune and evaluate BART-large model with embedding-based formulation, move to the embedding-based directory.

## Control Tokens

To fine-tune and evaluate any model with tagging-based formulation, move to the tagging-based directory. 

## Loading the models 
You can download the model checkpoints here:
* [Embedding-based formulation](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/EQuf0z9DiBpJlVDl6BJayy8By4oXGHmYD1fG1MqZs3YsxA?e=tIYkWY)
* [Tagging-based formulation](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/EQQDVckMfP5AkeVdCVSmyEkBC8BlJbvvbKd9ZMpmY6gypA?e=g7wBLo)
* [Prepend-based formulation](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/ESofGhUEXmhNgUHyEuxq0cMBR1Bism5qmNkmp1jBtZdsvw?e=NnVUhv)
* [Prepend and tagging-based formulation](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/EegP4M3cbHtNqLF7gglFIToBfIPNEzcguhdoBk8GePJTWg?e=TaWCEl)


## Get the data 

You can download the topic-assigned dataset based on CNN/DailyMail dataset (data directory) [here](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/EQuf0z9DiBpJlVDl6BJayy8By4oXGHmYD1fG1MqZs3YsxA?e=tIYkWY) and [here](https://aristotleuniversity-my.sharepoint.com/:u:/g/personal/scpassali_office365_auth_gr/EfoWdJU_uLdHtuQDre6WXWABISQAF15-1HpOcQSrQD6J6A?e=KRe8Z9).


## Generating topic-oriented summaries 
You can use the fine-tuned tagging-based model to generate topic-oriented summaries.

First, install the transformers library:
```
pip install transformers==4.11.0
```

Download and load model from disk

```python
>>> from transformers import BartForConditionalGeneration, BartTokenizer

>>> model = BartForConditionalGeneration.from_pretrained(MODEL_PATH, local_files_only=True)
>>> tokenizer = BartTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
```

Summarize any text, by simply tagging words of interest
```python
>>> text_to_summarize = '''A man accused of plotting to [TAG]attack[TAG] the U.S. Capitol called a television station from jail and said if he had n't been arrested he would have [TAG]gone[TAG] to Washington and shot [TAG]President[TAG] Barack [TAG]Obama[TAG] in the head . WXIX-TV in Cincinnati said Christopher Lee Cornell , 20 , called the station from the Kentucky jail where he 's being held , confessed to being a supporter of the [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]group[TAG] and said he [TAG]planned[TAG] to [TAG]kill[TAG] [TAG]government[TAG] officials in retaliation for U.S. [TAG]strikes[TAG] on the [TAG]militant[TAG] organization . A former Michigan high school football coach was arrested Friday and faces multiple charges including sending explicit [TAG]images[TAG] to students as young as 13 years old . The station [TAG]aired[TAG] part of the interview on Friday night , hours after Cornell 's attorney argued unsuccessfully in court that it could violate the defendant 's right to a fair trial . Scroll down for video . Louis Michael Rau , 46 , faces 12 charges including seven counts of distributing sexually explicit matter to a minor ; four counts of selling or furnishing alcohol to a minor ; and one count of accosting a minor for immoral purposes -- which is a four-year felony , the Morning Sun reports . Rau resigned from his position at the Beal [TAG]City[TAG] High School in January after complaints from parents about the coach 's alleged inappropriate conduct led to an investigation by the Isabella County Sheriff 's Department . Multiple Charges : Louis Rau , 46 ( photographed ) , was arrested Friday and faces multiple charges including sending explicit [TAG]images[TAG] to students as young as 13 years old . During the investigation , the department conducted several interviews and searched phones , tablets , cameras , computers , DVD 's , text messages and emails , Sheriff Leo Mioduszewski told MLive . The search found that Rau sent nude photos to five victims -- all student-athletes -- between 2011 and 2015 , [TAG]People[TAG] reports . Christopher Lee Cornell allegedly plotted to [TAG]attack[TAG] the U.S. Capitol in Washington and [TAG]kill[TAG] [TAG]government[TAG] officials inside it and spoke of his desire to [TAG]support[TAG] the [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]militant[TAG] [TAG]group[TAG] . One of the victims was 13 when the ex-coach began sending him the sexually explicit photos , and all of the others were under 18 years old . Cornell , asked by the interviewer what he would have done had he not been arrested in January , said he would have [TAG]taken[TAG] one of his guns , ' I would have put it to [TAG]Obama[TAG] 's head , I would have pulled the trigger , then I would unleash more bullets on the Senate and House of Representative members , and I would have [TAG]attacked[TAG] the Israeli embassy and various other buildings . ' Court records obtained by the Sun [TAG]state[TAG] that in addition to the photos , Rau gave the boys sex toys . Cornell , who repeatedly identified himself as Muslim , said he wanted to carry out the [TAG]attack[TAG] because of 'the continued [TAG]American[TAG] aggression against our [TAG]people[TAG] and the fact that [TAG]America[TAG] , specifically [TAG]President[TAG] [TAG]Obama[TAG] , wants to wage [TAG]war[TAG] against [TAG]Islamic[TAG] [TAG]State[TAG] . ' Rau reportedly once gave an eighth grader a toy 'described as a vagina with a tube . ' On four different occasions , the Sun reports , Rau purchased alcohol for three of the victims ; court records note that both text messages and Rau 's admission confirmed the purchases . Victims : The search found that Rau sent nude photos to five victims -- all student-athletes -- between 2011 and 2015 . He said : 'They might say I 'm a [TAG]terrorist[TAG] , but you [TAG]know[TAG] we see [TAG]American[TAG] [TAG]troops[TAG] as [TAG]terrorists[TAG] as well , coming to our land , stealing our resources and [TAG]killing[TAG] our [TAG]people[TAG] , raping our [TAG]women[TAG] . ' Cornell , also [TAG]known[TAG] as Raheel Mahrus Ubaydah , grew up in the Cincinnati suburbs and still lived with his parents . He said [TAG]support[TAG] of the [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]group[TAG] is widespread . 'We 're here in Ohio . Toys/Alcohol : Court records [TAG]state[TAG] that in addition to the photos , Rau also gave the boys sex toys and bought them alcohol . We 're in every [TAG]state[TAG] , ' he said . At Friday 's arraignment , Rau 's attorney , Dan O'Neill , described Rau as a 'home-grown boy ' and noted that the 46-year-old had no criminal record , the Sun reports . He spoke of Rau 's notoriety as 'the most celebrated football coach Beal [TAG]City[TAG] has ever had . ' Rau 's bail was set at $ 80,000 , lowered from $ 120,000 which was set during the time of his arrest , the Sun reports . Upon his resignation , Rau , who also served as a substitute teacher at the school , was banned from school [TAG]grounds[TAG] except for school board meetings and public elections held at the school , MLive reports . 'We 're more organized than you think . ' WXIX-TV in Cincinnati said Christopher Lee Cornell , 20 , called the station from the Kentucky jail where he 's being held , confessed to being a supporter of the [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]group[TAG] and said he [TAG]planned[TAG] to [TAG]kill[TAG] [TAG]government[TAG] officials in retaliation for U.S. [TAG]strikes[TAG] on the [TAG]militant[TAG] organization . He said that if he had n't been caught , he would have [TAG]attacked[TAG] , [TAG]President[TAG] Barack [TAG]Obama[TAG] , the Senate , the House of Representatives and many other places in the nation 's capital . As part of his bail conditions , Rau is not allowed in any school [TAG]zones[TAG] , not allowed to be in the presence of minors , not allowed to attend sporting events where minors or present , and is not allowed to contact the victims in any way , according to MLive . In 2006 , Rau received a 14-day unpaid suspension for allegedly slapping a player at a football banquet . Slap : In 2006 , Rau received a 14-day unpaid suspension for allegedly slapping a player at a football banquet . High School : A Beal [TAG]City[TAG] High School ( photographyed ) graduate , Rau began coaching at the school in 2000 and led the team to a [TAG]state[TAG] championship in 2009 . An investigation into the incident was [TAG]launched[TAG] after a concerned parent of a former-player wrote a letter detailing the July 2006 incident , saying several football players saw Rau slap the student in the face . Cornell , who repeatedly identified himself as Muslim , said he wanted to carry out the [TAG]attack[TAG] because of 'the continued [TAG]American[TAG] aggression against our [TAG]people[TAG] and the fact that [TAG]America[TAG] , specifically [TAG]President[TAG] [TAG]Obama[TAG] , wants to wage [TAG]war[TAG] against [TAG]Islamic[TAG] [TAG]State[TAG] ' At times what seemed like a nervous chuckle punctuated his responses . He said he would do whatever the [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]group[TAG] asked of him , including [TAG]beheading[TAG] Americans , and predicted 'there will be many , many [TAG]attacks[TAG] ' . A federal indictment charges Cornell with two counts that carry possible sentences of up to 20 years each upon conviction : attempted murder of [TAG]government[TAG] employees and officials and solicitation to commit a crime of violence . 'When I asked [ the victim ] about the incident myself , he said that , 'Yes . Mr. Rau b * * * * slapped me , '' the letter reads . A Beal [TAG]City[TAG] High School graduate , Rau began coaching at the school in 2000 and led the team to a [TAG]state[TAG] championship in 2009 . He also faces a firearms-related charge . He has pleaded not guilty and awaits trial in Cincinnati . Rau posted bail shortly after his arraignment Friday and is scheduled to appear in court Thursday for a probable cause hearing . Cornell was arrested outside a gun shop near his home on January 14 after the FBI said he bought two M-15 assault weapons and 600 rounds of ammunition . The FBI said in court documents that Cornell [TAG]planned[TAG] to 'wage jihad ' by [TAG]attacking[TAG] the Capitol with pipe [TAG]bombs[TAG] and shooting [TAG]government[TAG] officials and employees . Cornell was coerced and misled by ' a snitch ' trying to better his own legal situation , his father said . Cornell warned the news station that there were [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]group[TAG] supporters in almost all of the [TAG]United[TAG] States . Cornell was arrested outside a gun shop near his home on January 14 after the FBI said he bought two M-15 assault weapons and 600 rounds of ammunition . He described his son as a 'mommy 's boy ' who spent hours playing video games in his bedroom . He also said his son was 'at peace ' after becoming a practicing Muslim . 'He was dragged into this , ' Cornell said before the hearing . 'He was coerced . ' His son had long expressed distrust of [TAG]government[TAG] and the news media , and local police said he disrupted a 9/11 memorial ceremony in 2013 . The FBI said he had for months sent social media messages and posted video espousing [TAG]support[TAG] for [TAG]Islamic[TAG] [TAG]State[TAG] [TAG]militants[TAG] and for violent [TAG]attacks[TAG] by others . Cornell told an informant they should 'wage jihad , ' authorities said in court papers . Similar stings in recent years have led to accusations of entrapment . But the FBI has argued such stings are vital for averting deadly terror [TAG]attacks[TAG] , and juries have returned tough sentences . Cornell ( pictured left years ago ) posted messages on Twitter sympathizing with [TAG]Islamic[TAG] [TAG]terrorists[TAG] led to an undercover FBI operation . His father John Cornell ( right ) claims his son was coerced into the plot. '''
>>> output = model.generate(input_ids)
>>> print(tokenizer.decode(output[0])
```

## License 
This project is released under Apache 2.0 license.

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


