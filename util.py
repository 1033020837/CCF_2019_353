import re,jieba

stop_words_list = ['？','《','🔺','️?','!','#','%','%','，','Ⅲ','》','丨','、','）','（','​',
                '👍','。','😎','/','】','-','⚠️','：','✅','㊙️','“',')','(','！','🔥',',',
                '【','[',']']

def stop_words(x):
        try:
            x = x.strip()
        except:
            return ''
        x = re.sub('\?\?+','',x)
        x = re.sub('#+','',x)
        return x
         
def seg_depart(row, attribute_name):
    """
        分词
    """
    sentence = str(row[attribute_name])
    sentence_depart = jieba.cut(sentence.strip())
    outstr = ""
    for word in sentence_depart:
        if word in stop_words_list or word == "":
            continue
        outstr += word
        outstr += "  "
    return outstr
