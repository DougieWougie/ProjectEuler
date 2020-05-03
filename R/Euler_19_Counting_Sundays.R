a.date <- as.Date("1901/01/01")
end.date <- as.Date("2000/12/31")
count <- 0
while (a.date <= end.date) {
    if (format(a.date, "%d") == "01") {
        if (format(a.date, "%A") == "Sunday") {
            count = count + 1
        }
    }
    a.date = a.date + 1
}
print(count)
