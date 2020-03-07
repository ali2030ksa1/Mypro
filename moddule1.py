

import nltk
from nltk import word_tokenize

from nltk.stem.isri import ISRIStemmer

st = ISRIStemmer()

w= " البحث العلمي أو البحث أو التجربة التنموية هو أسلوب منظم في جمع المعلومات الموثوقة وتدوين الملاحظات والتحليل الموضوعي لتلك المعلومات باتباع أساليب ومناهج علمية محددة بقصد التأكد من صحتها أو تعديلها أو إضافة الجديد لها، ومن ثم التوصل إلى بعض القوانين والنظريات والتنبؤ بحدوث مثل هذه الظواهر والتحكم في أسبابها"

for a in word_tokenize(w):

    print(st.stem(a))