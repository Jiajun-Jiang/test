class ShoppingBag:

    def calculate_bag_total(self, items, discounts):
        # Your code goes here
        item={}
        discount={}
        after_dis={}
        for i in items:
            index=i[0:3]
            s='P'+index
            if item.get(index):
                item[index]+=1
                item[s]+=int(i[3:])
            else:
                 item[index]=1
                 item[s]=int(i[3:])

        print("before_item",item)
        for i in discounts:
            for j in item.keys():
                if i[0:3]==j:
                    if int(i[3])<=item.get(j):
                        if i[4]=='P':
                            res=item['P'+j]*(100-int(i[5:]))/100
                            if after_dis.get('P'+j):
                                if after_dis.get('P'+j)>res:
                                    after_dis['P'+j]=res
                            else:
                                after_dis['P'+j]=res
                        if i[4]=='C':
                            if int(i[5:])<=item['P'+j]:
                                res=item['P'+j]-int(i[5:])
                                if after_dis.get('P'+j):
                                    if after_dis.get('P'+j)>res:
                                        after_dis['P'+j]=res
                                else:
                                    after_dis['P'+j]=res
                            else:
                                continue
                    else:
                        continue
        total=0
        for j in after_dis.keys():
            if j in item.keys():
                item[j]=after_dis.get(j)
        for i in set(items):
          total+=item.get('P'+i[0:3])
          
        print("after_item",item)
        print("after_dis",after_dis)
        print("total",total)
        return total
        
