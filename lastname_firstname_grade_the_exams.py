import re
files_name=input("vui long nhap ten file:")
def data(data_raw): #nhap dư lieu doc duoc vao list
    list_raw=[]
    with open(data_raw) as rf:
        for i in rf:
            i = i.rstrip()
            list_raw.append(i)
    return list_raw
def data_clean(list_raw): # lam sach du lieu doc duoc
    list_clean=[]
    for j in range(len(list_raw)):
        comma = ','
        x = list_raw[j].split(comma)
        list_clean.append(x)
    return list_clean
def kiemtra_ten(f):
    regex='[N]{1,1}[0-9]{8,8}'
    x=re.findall(regex,f)
    if len(x)==0:
        return False
    else:
        return True
#------------------------Task2----------------------------------------
def valid_invalid(list_raw,list_clean):
    valid = 0
    invalid = 0
    loi_ten = []
    loi_dap_an = []
    for i in range(len(list_clean)):
        if len(list_clean[i]) == 26:
            if kiemtra_ten(list_clean[i][0]) == True:
                valid = valid + 1
            else:
                invalid = invalid + 1
                loi_ten.append(list_raw[i])
        else:
            invalid = invalid + 1
            loi_dap_an.append(list_raw[i])
            if kiemtra_ten(list_clean[i][0]) == False:
                loi_ten.append(list_raw[i])
    print('so dong nhap dung la:',valid)
    print('so dong nhap sai la:',invalid)
    print('cac dong nhap khong dung so dap an la:')
    for i in loi_dap_an:
        print(i)
    print('cac dong nhap sai ten la:')
    for i in loi_ten:
        print(i)
#------------Task3--------------------------------------------
def tinh_diem(list_clean): # tinh diem cho tung hoc sinh
    final_mark=[]
    tong_hop=[]
    answer_key = ['dap_an','B','A','D','D','C','B','D','A','C','C','D','B','A','B','A','C','B','D','A','C','A','A','B','D','D']
    list_skip=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #dem so cau bi bo qua
    list_false=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #dem so cau sai
    bo_qua=[]
    lam_sai=[]
    for i in range(len(list_clean)):
        mark=0
        if len(list_clean[i]) == 26 and kiemtra_ten(list_clean[i][0]) == True:
            for j in range(1,26):
                if list_clean[i][j]==answer_key[j]:
                    mark =mark+4
                elif list_clean[i][j]=='':
                    mark =mark+0
                    list_skip[j-1]=list_skip[j-1]+1
                else:
                    mark=mark-1
                    list_false[j-1]=list_false[j-1]+1
        final_mark.append(mark)
    dem_diem_cao=0
    diem_tong=0
    for diem in final_mark:
        if diem > 80:
            dem_diem_cao = dem_diem_cao + 1
    for i in final_mark:
        diem_tong = diem_tong + i
    #tinh diem trung binh
    avg_point=round(diem_tong/len(final_mark),2)
    n=len(final_mark)
    #tinh diem cao nhat, thap nhat
    max_point=max(final_mark)
    min_point=min(final_mark)
    #tinh range diem
    range_point=max_point-min_point
    #tinh trung vi
    if n%2==0:
        median=(final_mark[int(n/2)]+final_mark[int(n/2)+1])/2
    else:
        median=final_mark[int((n+1)/2)]
    #tim cau bi bo qua nhieu nhat
    for i in range(len(list_skip)):
        if list_skip[i]==max(list_skip):
            bo_qua.append(i+1)
    #tim cau sai nhieu nhat
    for i in range(len(list_false)):
        if list_false[i]==max(list_false):
            lam_sai.append(i+1)
    tong_hop.append(final_mark)
    tong_hop.append(dem_diem_cao)
    tong_hop.append(avg_point)
    tong_hop.append(max_point)
    tong_hop.append(min_point)
    tong_hop.append(range_point)
    tong_hop.append(median)
    tong_hop.append(bo_qua)
    tong_hop.append(max(list_skip))
    tong_hop.append(lam_sai)
    tong_hop.append(max(list_false))
    return tong_hop
#-----------------task4--------------------------------------------
def nhap_diem(files_name,list_clean,final_mark): # nhap diem vao file moi
    ten_hs=[]
    for b in list_clean:
        ten_hs.append(b[0])
    with open(files_name[:len(files_name)-4]+'_grades.txt','w') as wf:
        for i in range(len(list_clean)):
            wf.write(str(ten_hs[i]))
            wf.write(',')
            wf.write(str(final_mark[i]))
            wf.write('\n')
    print('done')
#----------------task1--------------------------------------------
try:
    list_raw=data(files_name)
    list_clean=data_clean(list_raw)
    valid_invalid(list_raw,list_clean)
    tong_hop=tinh_diem(list_clean)
    print('***Report***')
    print('Tong so hoc sinh co diem cao nhat:', tong_hop[1])
    print('Diem trung binh cua lop hoc la:', tong_hop[2])
    print('Diem cao nhat la:', tong_hop[3])
    print('Diem thap nhat la:', tong_hop[4])
    print('Mien gia tri cua diem la:', tong_hop[5])
    print('Gia tri trung vi la:', tong_hop[6])
    print('Cau bi bo qua nhieu nhat: {} - {} - {}'.format(tong_hop[7], tong_hop[8], round(tong_hop[8] / len(tong_hop[0]),2)))
    print('Cau bi lam sai nhieu nhat: {} - {} - {}'.format(tong_hop[9], tong_hop[10], round(tong_hop[10] / len(tong_hop[0]),2)))
    nhap_diem(files_name,list_clean,tong_hop[0])
except FileNotFoundError:
    print('Khong tim thay tep')














