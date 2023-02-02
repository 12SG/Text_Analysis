#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Make a request to the webpage
url =requests.get("https://docs.google.com/spreadsheets/d/1D7QkDHxUSKnQhR--q0BAwKMxQlUyoJTQ/edit#gid=823090326")


# In[3]:


# Parse the HTML of the webpage
soup = BeautifulSoup(url.content, 'html.parser')


# In[4]:


soup.title.string


# In[5]:


import textblob
import bs4


# In[6]:


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55'}


# In[7]:


soup = bs4.BeautifulSoup(url.text,'lxml')


# In[8]:


soup = soup.getText(strip=True)


# In[9]:


soup


# # Data Analysis 

# In[10]:


import pandas as pd


# In[11]:


Output_Data_Structure ={"Input.xlsx - Google SheetsJavaScript isn't enabled in your browser, so this file can't be opened. Enable and reload.InputShareSign inThe version of the browser you are using is no longer supported. Please upgrade to asupported browser.DismissFileEditViewInsertFormatDataToolsFormHelpAccessibilityUnsaved changes to DriveSee new changesAccessibilityView onlyABCDEFGHIJKLMNOPQRSTUVWXYZ1URL_IDURL237https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/338https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/439https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/540https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/641https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/742https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/843https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/944https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/1045https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/1146https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/1247https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/1348https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/1449https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/1550https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/1651https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/1752https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/1853https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/1954https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/2055https://insights.blackcoffer.com/evolution-of-advertising-industry/2156https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/2257https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/2358https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/2459https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/2560https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/2661https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/2762https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/2863https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/2964https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/3065https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/3166https://insights.blackcoffer.com/how-we-forecast-future-technologies/3267https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/3368https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/3469https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/3570https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/3671https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/3772https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/3873https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/3974https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/4075https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/4176https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/4277https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/4378https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/4479https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/4580https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/4681https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/4782https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/4883https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/4984https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/5085https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/5186https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/5287https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/5388https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/5489https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/5590https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/5691https://insights.blackcoffer.com/human-rights-outlook/5792https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/5893https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/5994https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/6095https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/6196https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/6297https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/6398https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/6499https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/65100https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/66101https://insights.blackcoffer.com/travel-and-tourism-outlook/67102https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/68103https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/69104https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/70105https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/71106https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/72107https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/73108https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/74109https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/75110https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/76111https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/77112https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/78113https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/79114https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/80115https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/81116https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/82117https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/83118https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/84119https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/85120https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/86121https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/87122https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/88123https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/89124https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/90125https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/91126https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/92127https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/93128https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/94129https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/95130https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/96131https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/97132https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/98133https://insights.blackcoffer.com/continued-demand-for-sustainability/99134https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/100135https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/Quotes are not sourced from all markets and may be delayed by up to 20 minutes. Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice.DisclaimerSheet1A browser error has occurred.Please press Ctrl-F5 to refresh the page and try again.A browser error has occurred.Please hold the Shift key and click the Refresh button to try again."}


# In[12]:


df = pd.DataFrame(Output_Data_Structure)


# In[13]:


df.to_excel('Output_Data_Structure.xlsx', index=False)


# In[14]:


DF = pd.read_excel('Output_Data_Structure.xlsx')


# In[15]:


print(DF)


# ## Sentiment Analysis 

# In[16]:


import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


# In[17]:


nltk.download('vader_lexicon')


# In[18]:


# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


# In[19]:


text = "Input.xlsx - Google SheetsJavaScript isn't enabled in your browser, so this file can't be opened. Enable and reload.InputShareSign inThe version of the browser you are using is no longer supported. Please upgrade to asupported browser.DismissFileEditViewInsertFormatDataToolsFormHelpAccessibilityUnsaved changes to DriveSee new changesAccessibilityView onlyABCDEFGHIJKLMNOPQRSTUVWXYZ1URL_IDURL237https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/338https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/439https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/540https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/641https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/742https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/843https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/944https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/1045https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/1146https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/1247https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/1348https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/1449https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/1550https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/1651https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/1752https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/1853https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/1954https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/2055https://insights.blackcoffer.com/evolution-of-advertising-industry/2156https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/2257https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/2358https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/2459https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/2560https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/2661https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/2762https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/2863https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/2964https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/3065https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/3166https://insights.blackcoffer.com/how-we-forecast-future-technologies/3267https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/3368https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/3469https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/3570https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/3671https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/3772https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/3873https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/3974https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/4075https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/4176https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/4277https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/4378https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/4479https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/4580https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/4681https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/4782https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/4883https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/4984https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/5085https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/5186https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/5287https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/5388https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/5489https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/5590https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/5691https://insights.blackcoffer.com/human-rights-outlook/5792https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/5893https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/5994https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/6095https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/6196https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/6297https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/6398https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/6499https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/65100https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/66101https://insights.blackcoffer.com/travel-and-tourism-outlook/67102https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/68103https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/69104https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/70105https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/71106https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/72107https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/73108https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/74109https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/75110https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/76111https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/77112https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/78113https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/79114https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/80115https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/81116https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/82117https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/83118https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/84119https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/85120https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/86121https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/87122https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/88123https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/89124https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/90125https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/91126https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/92127https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/93128https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/94129https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/95130https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/96131https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/97132https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/98133https://insights.blackcoffer.com/continued-demand-for-sustainability/99134https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/100135https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/Quotes are not sourced from all markets and may be delayed by up to 20 minutes. Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice.DisclaimerSheet1A browser error has occurred.Please press Ctrl-F5 to refresh the page and try again.A browser error has occurred.Please hold the Shift key and click the Refresh button to try again."


# ### Positive Score 

# In[20]:


score = sia.polarity_scores(text)


# In[21]:


print("Positive score: ",score['pos'])


# ### Negative Score 

# In[22]:


print("Negative score: ",score['neg'])


# ### Polarity Score 

# In[23]:


print("Polarity score: ",score['compound'])


# ### Subjectivity Score

# In[24]:


pip install textblob


# In[25]:


from textblob import TextBlob


# In[26]:


blob = TextBlob(text)


# In[27]:


subjectivity_score = blob.sentiment.subjectivity


# In[28]:


print("Subjectivity score: ", subjectivity_score)


# ### Average Sentence Length

# In[29]:


from nltk.tokenize import sent_tokenize


# In[30]:


sentences = sent_tokenize(text)


# In[31]:


total_length = 0
for sentence in sentences:
    total_length += len(sentence)
average_length = total_length / len(sentences)


# In[32]:


print("Average Sentence Length: ", average_length)


# ### Percentage Of Complex Words 

# In[33]:


from nltk.corpus import cmudict


# In[34]:


from nltk.tokenize import word_tokenize
nltk.download('cmudict')
nltk.download('punkt')


# In[35]:


text = "Input.xlsx - Google SheetsJavaScript isn't enabled in your browser, so this file can't be opened. Enable and reload.InputShareSign inThe version of the browser you are using is no longer supported. Please upgrade to asupported browser.DismissFileEditViewInsertFormatDataToolsFormHelpAccessibilityUnsaved changes to DriveSee new changesAccessibilityView onlyABCDEFGHIJKLMNOPQRSTUVWXYZ1URL_IDURL237https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/338https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/439https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/540https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/641https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/742https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/843https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/944https://insights.blackcoffer.com/how-neural-networks-can-be-applied-in-various-areas-in-the-future/1045https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/1146https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/1247https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/1348https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/1449https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/1550https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/1651https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/1752https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/1853https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/1954https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/2055https://insights.blackcoffer.com/evolution-of-advertising-industry/2156https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/2257https://insights.blackcoffer.com/covid-19-environmental-impact-for-the-future/2358https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/2459https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/2560https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/2661https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/2762https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/2863https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/2964https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/3065https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/3166https://insights.blackcoffer.com/how-we-forecast-future-technologies/3267https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/3368https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/3469https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/3570https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/3671https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/3772https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/3873https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/3974https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/4075https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/4176https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/4277https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/4378https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/4479https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/4580https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/4681https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/4782https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/4883https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/4984https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/5085https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/5186https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/5287https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/5388https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/5489https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/5590https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/5691https://insights.blackcoffer.com/human-rights-outlook/5792https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/5893https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/5994https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/6095https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/6196https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/6297https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/6398https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/6499https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/65100https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/66101https://insights.blackcoffer.com/travel-and-tourism-outlook/67102https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/68103https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/69104https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/70105https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-office-space-and-co-working-industries/71106https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/72107https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/73108https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/74109https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/75110https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/76111https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/77112https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/78113https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/79114https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/80115https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/81116https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/82117https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/83118https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/84119https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/85120https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/86121https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/87122https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/88123https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/89124https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/90125https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/91126https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/92127https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/93128https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/94129https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/95130https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/96131https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/97132https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/98133https://insights.blackcoffer.com/continued-demand-for-sustainability/99134https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/100135https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/Quotes are not sourced from all markets and may be delayed by up to 20 minutes. Information is provided 'as is' and solely for informational purposes, not for trading purposes or advice.DisclaimerSheet1A browser error has occurred.Please press Ctrl-F5 to refresh the page and try again.A browser error has occurred.Please hold the Shift key and click the Refresh button to try again."


# In[36]:


d = cmudict.dict()


# In[37]:


words = word_tokenize(text)


# In[38]:


complex_word_count = 0
complex_word_count += 1


# In[39]:


percentage_of_complex_words = (complex_word_count/len(words))*100


# In[40]:


print("Percentage of complex words: ", percentage_of_complex_words)


# ### Avg Number of words per sentence 

# In[42]:


nltk.download('punkt')


# In[43]:


Sentences = nltk.sent_tokenize(text) 


# In[44]:


total_words = 0


# In[47]:


for Sentence in Sentences:
    words = nltk.word_tokenize(Sentence)
    total_words += len(words)


# In[49]:


avg_words_per_sentence = total_words / len(Sentences)


# In[50]:


print(avg_words_per_sentence)


# ###  Complex Word Count

# In[51]:


cmu_dict = nltk.corpus.cmudict.dict()


# In[56]:


Sentences = nltk.sent_tokenize(text)


# In[57]:


complex_word_count = 0


# In[67]:


for Sentence in Sentences:
     words = nltk.word_tokenize(Sentence)
    


# In[68]:


for word in words:
        syllable_count = cmu_dict.get(word.lower())
        if syllable_count is not None:
            if len(syllable_count[0]) >=3:
                complex_word_count +=1


# In[69]:


print("Number of complex words: ",complex_word_count)


# ### Word Count 

# In[70]:


word_count = len(words)


# In[71]:


print(word_count)


# ### Syllable Per Word

# In[76]:


total_syllables = 0
total_words = 0


# In[80]:


for word in words:
    total_words+=1
    syllable_count = cmu_dict.get(word.lower())
    if syllable_count is not None:
        total_syllables += len(syllable_count[0])


# In[81]:


avg_syllables_per_word = total_syllables / total_words


# In[82]:


print("Average Syllables Per Word: ",avg_syllables_per_word)


# ### Personal Pronouns

# In[90]:


personal_pronouns =["I", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them"]


# In[91]:


personal_pronoun_count = 0


# In[92]:


for sentence in sentences:
    words = nltk.word_tokenize(sentence)


# In[93]:


for word in words:
    if word.lower() in personal_pronouns:
            personal_pronoun_count += 1


# In[94]:


print("Number of personal pronouns: ", personal_pronoun_count)


# ### Average Word Length 

# In[95]:


total_characters = 0


# In[96]:


for word in words:
    total_characters += len(word)


# In[100]:


avg_word_length = total_characters / len(words)
print("Average word length: ", avg_word_length)

