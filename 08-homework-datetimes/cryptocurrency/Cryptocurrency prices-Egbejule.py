{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Cryptocurrency prices\n",
    "\n",
    "* **Filename:**  `cryptocurrencies.csv`\n",
    "* **Description:** Cryptocurrency prices for a handful of coins over time.\n",
    "* **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)\n",
    "\n",
    "### Make a chart of bitcoin's high, on a weekly basis\n",
    "\n",
    "You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.\n",
    "\n",
    "*Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/eromoegbejule/.pyenv/versions/3.8.2/lib/python3.8/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.\n",
      "  warnings.warn(msg)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv (\"cryptocurrencies.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date</th>\n",
       "      <th>open</th>\n",
       "      <th>high</th>\n",
       "      <th>low</th>\n",
       "      <th>close</th>\n",
       "      <th>volume</th>\n",
       "      <th>market_cap</th>\n",
       "      <th>coin</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-02-12</td>\n",
       "      <td>8,141.43</td>\n",
       "      <td>8,985.92</td>\n",
       "      <td>8,141.43</td>\n",
       "      <td>8,926.57</td>\n",
       "      <td>6,256,440,000</td>\n",
       "      <td>137,258,000,000</td>\n",
       "      <td>BTC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-02-11</td>\n",
       "      <td>8,616.13</td>\n",
       "      <td>8,616.13</td>\n",
       "      <td>7,931.10</td>\n",
       "      <td>8,129.97</td>\n",
       "      <td>6,122,190,000</td>\n",
       "      <td>145,245,000,000</td>\n",
       "      <td>BTC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-02-10</td>\n",
       "      <td>8,720.08</td>\n",
       "      <td>9,122.55</td>\n",
       "      <td>8,295.47</td>\n",
       "      <td>8,621.90</td>\n",
       "      <td>7,780,960,000</td>\n",
       "      <td>146,981,000,000</td>\n",
       "      <td>BTC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-02-09</td>\n",
       "      <td>8,271.84</td>\n",
       "      <td>8,736.98</td>\n",
       "      <td>7,884.71</td>\n",
       "      <td>8,736.98</td>\n",
       "      <td>6,784,820,000</td>\n",
       "      <td>139,412,000,000</td>\n",
       "      <td>BTC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-02-08</td>\n",
       "      <td>7,637.86</td>\n",
       "      <td>8,558.77</td>\n",
       "      <td>7,637.86</td>\n",
       "      <td>8,265.59</td>\n",
       "      <td>9,346,750,000</td>\n",
       "      <td>128,714,000,000</td>\n",
       "      <td>BTC</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        date      open      high       low     close         volume  \\\n",
       "0 2018-02-12  8,141.43  8,985.92  8,141.43  8,926.57  6,256,440,000   \n",
       "1 2018-02-11  8,616.13  8,616.13  7,931.10  8,129.97  6,122,190,000   \n",
       "2 2018-02-10  8,720.08  9,122.55  8,295.47  8,621.90  7,780,960,000   \n",
       "3 2018-02-09  8,271.84  8,736.98  7,884.71  8,736.98  6,784,820,000   \n",
       "4 2018-02-08  7,637.86  8,558.77  7,637.86  8,265.59  9,346,750,000   \n",
       "\n",
       "        market_cap coin  \n",
       "0  137,258,000,000  BTC  \n",
       "1  145,245,000,000  BTC  \n",
       "2  146,981,000,000  BTC  \n",
       "3  139,412,000,000  BTC  \n",
       "4  128,714,000,000  BTC  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.date = pd.to_datetime(df.date)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
