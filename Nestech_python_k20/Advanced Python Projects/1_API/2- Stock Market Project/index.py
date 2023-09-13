import requests
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint and parameters / Xác định điểm cuối API và các tham số
api_endpoint = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'AAPL',
    'apikey': 'PR4W5934BIH8W33M'
}

# Send the request to the API / Gửi yêu cầu đến API
response = requests.get(api_endpoint, params=params)

# Parse the JSON response and convert it to a Pandas DataFrame 
# --Phân tích phản hồi của JSON và chuyển đổi nó thành một khung dữ liệu gấu trúc
data = pd.DataFrame.from_dict(response.json()['Time Series (Daily)'], orient='index')
data = data.astype(float)
print(data) 
# Plot the closing prices / Vẽ đồ thị giá đóng cửa
plt.plot(data['4. close'])
plt.title('AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


# Dòng này chuyển đổi đối tượng JSON trong phản hồi response từ API thành một khung dữ liệu Pandas data.

# Cụ thể, response.json() trả về một đối tượng JSON chứa thông tin giá cổ phiếu hàng ngày từ API.
#  Sau đó, ta truy cập vào khóa "Time Series (Daily)" bằng cách sử dụng cú pháp response.json()['Time Series (Daily)'] 
# để truy xuất các giá trị giá cổ phiếu hàng ngày từ đối tượng JSON

# Hàm pd.DataFrame.from_dict() chuyển đổi các giá trị từ đối tượng JSON thành một khung dữ liệu Pandas. 
# Tham số orient='index' cho biết rằng các chỉ số của khung dữ liệu được lấy từ các khóa của đối tượng JSON.

# Do đó, dòng lệnh này tạo ra một khung dữ liệu Pandas data chứa thông tin về giá cổ phiếu hàng ngày, 
# với các ngày được sắp xếp theo thứ tự tăng dần làm chỉ số của các hàng.