In this example, we're using the requests library to make a GET request to the OpenWeatherMap API. You'll need to replace YOUR_API_KEY_HERE with your actual API key, 
which you can obtain by signing up for a free account on the OpenWeatherMap website.

We're also specifying the city we want to fetch weather data for (in this case, New York), as well as the units we want the data to be returned in (imperial).


If the API request is successful (i.e. the response status code is 200), we extract the relevant weather data (temperature, humidity, and description) from the JSON response and print it to the console.


Trong ví dụ này, chúng tôi đang sử dụng thư viện yêu cầu để thực hiện yêu cầu nhận API OpenWeathermap.Bạn sẽ cần thay thế your_api_key_here bằng khóa API thực tế của bạn,
mà bạn có thể có được bằng cách đăng ký tài khoản miễn phí trên trang web OpenWeathermap.

Chúng tôi cũng chỉ định thành phố mà chúng tôi muốn lấy dữ liệu thời tiết (trong trường hợp này là New York), cũng như các đơn vị chúng tôi muốn dữ liệu được trả lại trong (Imperial).


Nếu yêu cầu API thành công (nghĩa là mã trạng thái phản hồi là 200), chúng tôi trích xuất dữ liệu thời tiết có liên quan (nhiệt độ, độ ẩm và mô tả) từ phản hồi JSON và in nó vào bảng điều khiển.