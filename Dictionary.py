telephone_directory = {
    "Arjun Mehta": "+919812345678",
    "Priya Sharma": "+919321234567",
    "Ravi Kumar": "+919876543210",
    "Neha Gupta": "+919090123456",
    "Vinay Reddy": "+919543210987",
    "Sneha Kapoor": "+919988765432",
    "Ankit Verma": "+919123456789",
    "Divya Nair": "+919345678901",
    "Rohan Singh": "+919870123456",
    "Pooja Jain": "+919112367890",
    "Amit Khanna": "+919887654321",
    "Sakshi Patel": "+919344567890",
    "Manoj Desai": "+919456789012",
    "Sonal Aggarwal": "+919523456789",
    "Nikhil Bansal": "+919234567891",
    "Geeta Iyer": "+919643210987",
    "Rajeev Arora": "+919532109876",
    "Rita Rao": "+919976543210",
    "Sunil Joshi": "+919321056789",
    "Megha Das": "+919443219876",
    "Rahul Chandra": "+919875432109",
    "Kavita Singh": "+919012345678",
    "Ajay Menon": "+919456789023",
    "Preeti Rao": "+919832176548",
    "Rakesh Jain": "+919983746251",
    "Suman Bhattacharya": "+919736482915",
    "Meera Pillai": "+919453827691",
    "Ashok Mehta": "+919675849302",
    "Lavanya Sharma": "+919654327891",
    "Vikram Bedi": "+919854627930",
    "Asha Dixit": "+919934587261",
    "Yash Goel": "+919862437981",
    "Snehal Deshmukh": "+919124578362",
    "Nisha Malhotra": "+919726489031",
    "Umesh Pathak": "+919985746238",
    "Deepak Tyagi": "+919826341759",
    "Kiran Varma": "+919364829570",
    "Pankaj Anand": "+919724581639",
    "Maya Pandey": "+919134728506",
    "Saurabh Sen": "+919937582461",
    "Anjali Khurana": "+919765328947",
    "Naveen Rathi": "+919836457219",
    "Priti Shah": "+919687452093",
    "Sameer Nanda": "+919823647015",
    "Kriti Kapoor": "+919674328591",
    "Aarav Nair": "+919874652301",
    "Mahesh Patil": "+919527463819",
    "Vijay Sood": "+919874152960",
    "Radhika Chopra": "+919726581490",
    "Govind Yadav": "+919635847290",
    "Reena Das": "+919824376510"
}

telephone_directory["Rohith Reddy"] = "+917546334589"
for k,v in telephone_directory.items():
    print(k,":",v)
print("Total Contacts:",len(telephone_directory))
print("Rohith Reddy" in telephone_directory)