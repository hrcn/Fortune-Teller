def generate_text(text, score):
    if 'model' in globals():
        pass
    else:
        from gensim.models import KeyedVectors
        model = KeyedVectors.load('GoogleNews-vectors-gensim-normed.bin', mmap='r')
        model.vectors_norm = model.vectors  # prevent recalc of normed vectors
        import re
        import pymysql
        import nltk
        import math
        from nltk.corpus import stopwords
        from wordfreq import word_frequency

        
    def text_input(text):   
        text = text.lower()
        text = re.sub("[!@?#$+%*:()'-/]", ' ', text)

        text = text.split(" ")
        head = text[0]
        word_list = []
        for i in text:
            if i == "": continue
            if i not in set(stopwords.words('english')):
                word_list.append(i)

        return word_list, head

    def classify(word_list):
        label_dict = {}
        for i in word_list:
            dist = 0
            for j in ["luck", "romance", "career", "finance", "friendship", "health"]:
                try:
                    cal_dist = model.similarity(i, j)
                    if cal_dist > dist:
                        dist = cal_dist
                        cur_word_label = j
                        wf = (math.log(word_frequency(i, "en")))**2
                except:
                    continue
            try:        
                if dist < 0.1: continue
                if cur_word_label in label_dict:
                    label_dict[cur_word_label].append(dist*wf)
                else:
                    label_dict[cur_word_label] = [dist*wf]
            except: pass
        return label_dict

    def predict(label_dict):
        label_list = []
        if label_dict == {}: return ["luck"]
        sum_val = 0
        for k, v in label_dict.items():
            if sum(v) > 20:
                label_list.append(k)
    
        if label_list == []: return ["luck"]
        return label_list
    
    def connect_sql(label_list):
        mydb = pymysql.connect(host="localhost",
                               user="root",
                               passwd="e124676136",
                               database="prediction")

        myresult = []
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM Suggestion")
        myresult.append(mycursor.fetchall())
        mycursor.execute("SELECT * FROM Score")
        myresult.append(mycursor.fetchall())
        

        total_score = int(score)
        # print(total_score)

        suggestion = []
        suggestion.append(total_score)
        
        for i in label_list:
            if i == "romance": suggestion.append(myresult[0][total_score][3])
            if i == "career": suggestion.append(myresult[0][total_score][4])
            if i == "finance": suggestion.append(myresult[0][total_score][5])
            if i == "health": suggestion.append(myresult[0][total_score][6])
            if i == "friendship": suggestion.append(myresult[0][total_score][7])
            if i == "luck": suggestion.append(myresult[0][total_score][8])
        
        return suggestion

    def response(label_list, head, suggestion):
        respon = """By Integrated Divination your """
        for i in label_list:
            respon += i
            respon += " "
        if suggestion[0] <= 25: respon += " 's condition is going on a worst trend, "
        if suggestion[0] <= 50 & suggestion[0] > 25: respon += " 's condition is going on a bad trend, "
        if suggestion[0] <= 75 & suggestion[0] > 50: respon += " 's condition is going on a good trend, "
        if suggestion[0] <= 100 & suggestion[0] > 75: respon += " 's condition is going on a best trend, "
            
            
        if head in ["is", "are", "am", "was", "were", "do", "does", "did", "shall", "should", "will", "would", "can", "could"]:
            if suggestion[0] > 50:
                respon = "Yes, " + respon
            else:
                respon = "No ," + respon
        respon = respon + "and here are some suggestion:"
        
        for k, v in enumerate(suggestion):
            if k == 0: continue
            respon += v
                
        return respon


#     print("please type in your question or keywords: (If you want to know a specific category, just type the name of category)")
    word_list, head = text_input(text)
    label_dict = classify(word_list)
    label_list = predict(label_dict)
    suggestion = connect_sql(label_list)
    respon = response(label_list, head, suggestion)

    return respon