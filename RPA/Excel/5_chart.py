from openpyxl import load_workbook
wb = load_workbook("3_input_cell.xlsx")
ws = wb.active

from openpyxl.chart import BarChart, LineChart, Reference
bar_value = Reference(ws, min_row=1, max_row=10, min_col=3, max_col=4 ) # Reference 를 통해서 참조할 워크시트와 자료의 좌표범위를 지정
# *GUI는 큰값에서 작은값으로 드래그가 가능하지만, 실제로는 min의 값이 max의 값보다 작아야한다
bar_chart = BarChart() # 차트객체를 생성하고 차트의 종류를 지정
#line_chart = LineChart()
bar_chart.add_data(bar_value,titles_from_data=True) # 참고값을 넣어둔 변수를 데이터로써 차트에 추가, titles_from_data 옵션은 지정 값에서 계열을 읽어, 차트의 표시해준다. 기본값은 F
bar_chart.style = 4 # 이미 있는 스타일 적용, 사용자의 개별 스타일 지정 가능
bar_chart.title = 'Chart Test' # 차트 이름
bar_chart.x_axis.title = 'Order' # X축 이름
bar_chart.y_axis.title = 'Grade' # X축 이음

ws.add_chart(bar_chart,"F2") # 차트와 삽입좌표를 지정하여 차트를 엑셀에 추가
print(bar_value)

wb.save("3_input_cell.xlsx")