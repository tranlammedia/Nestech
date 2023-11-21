import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Đọc dữ liệu từ file Excel
file_path = '/home/tranlam/Documents/Nestech/Nestech_python_k20/machinelearning/DataTim.csv'  # Thay đổi đường dẫn đến tệp Excel
data = pd.read_csv(file_path)

# Hiển thị dữ liệu đọc được từ file Excel
df = data #pd.DataFrame(data=data)
print(df.head())

def transform_data(data):
    
    # Tạo pipeline cho việc chuyển đổi dữ liệu string thành số
    string_pipeline = Pipeline([
        ('encoder', OrdinalEncoder())
    ])

    # Xác định các cột chứa dữ liệu string cần chuyển đổi
    string_columns = data.columns
    
    # Tạo ColumnTransformer để xử lý các cột riêng biệt
    preprocessor = ColumnTransformer(
        transformers=[
            ('string', string_pipeline, string_columns)
        ],
        remainder='passthrough'  # Giữ lại các cột không được chuyển đổi
    )
    # Fit và chuyển đổi dữ liệu của DataFrame
    transformed_data = preprocessor.fit_transform(data)
    df_transform = pd.DataFrame(transformed_data)

    return df_transform

df_transform = transform_data(df)

# Xác định cột nhãn và tên các cột đặc trưng
label_column = df_transform.columns[-1]  # Thay 'TenNhan' bằng tên cột nhãn của 
feature_columns = df_transform.columns[1:-1] # Thay ['TenCot1', 'TenCot2', 'TenCot3'] bằng tên các cột đặc trưng 

# Tách dữ liệu thành đặc trưng và nhãn
X = df_transform[feature_columns]
y = df_transform[label_column]

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Xây dựng mô hình cây quyết định
model = DecisionTreeClassifier(criterion='gini')  # Sử dụng chỉ số Gini
model.fit(X_train, y_train)

# # Dự đoán nhãn cho tập kiểm tra
predictions = model.predict(X_test)


# # Đánh giá độ chính xác của mô hình
accuracy = accuracy_score(y_test, predictions)
print(f"Độ chính xác của mô hình: {accuracy}")
print(classification_report(y_test,predictions))