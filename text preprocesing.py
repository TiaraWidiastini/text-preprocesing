import string
import re  # regex library
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

text = "Mecaru adalah upacara yang dilaksanakan untuk menjaga keharmonisan antara manusia dengan alam oleh umat Hindu di Bali, Indonesia.[1] Upacara mecaru juga disebut dengan Bhuta Yadnya.[1] Bhuta Yadnya pada hakikatnya merawat lima unsur alam, yakni tanah, air, udara, api, dan ether.[1] Upacara mecaru dilaksanakan sebelum hari raya Nyepi pada waktu Sasih Kesanga.[2] Upacara mecaru biasanya dilaksanakan di perempatan jalan dan di lingkungan rumah.[2] Setiap mengadakan upacara ini, setiap keluarga membuat caru atau persembahan sesuai dengan kemampuan ekonomi.[2] Persembahan tersebut merupakan penyucian Bhuta Kala dan segala kotoran yang ada, serta sebagai pengharapan segala keburukan tidak dialami lagi pada masa mendatang.[2] Persembahan dalam upacara mecaru biasanya berupa nasi lima warna, lauk-pauk ayam, brumbuhan, dan disertai tuak.[2] Upacara mecaru bertujuan untuk menanamkan nilai-nilai luhur dan spiritual kepada manusia agar selalu menjaga dan merawat alam dan lingkungan sekitarnya.[1] Masyarakat Bali percaya bahwa jika manusia merusak alam dan lingkungan, maka suatu saat nanti manusia akan dibinasakan oleh alam.[1]"

# lower case
lower_case = text.lower()
print(lower_case)

# remove number
number = re.sub(r"\d+", "", lower_case)
print(number)

# remove punctuation
punctuation = number.translate(str.maketrans("", "", string.punctuation))
print(punctuation)

# remove whitepace
whitepace = punctuation.strip()
print(whitepace)

# tokenize
tokenize = whitepace.split()
print(tokenize)

# remove stopword
listStopword = set(stopwords.words('indonesian'))
removed = []
for t in tokenize:
    if t not in listStopword:
        removed.append(t)
print(removed)

# stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()
result = stemmer.stem(whitepace)
result = word_tokenize(result)
print(result)
