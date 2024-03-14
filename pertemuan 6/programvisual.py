import matplotlib.pyplot as plt


# Fungsi untuk menghasilkan plot fungsi kuadrat
def plot_kuadrat():
    x = range(-10, 11)  
    y = [i ** 2 for i in x]  

    plt.plot(x, y, label='y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot Fungsi Kuadrat')
    plt.grid(True)  
    plt.legend()  
    plt.show()  

# Fungsi untuk menyoroti titik-titik yang memenuhi kondisi tertentu
def highlight_points():
    x = range(-10, 11)  
    y = [i ** 2 for i in x]  

    plt.plot(x, y, label='y = x^2') 

    # Menyoroti titik-titik yang memenuhi kondisi tertentu
    for i in x:
        if i % 2 == 0 and i != 0: 
            plt.scatter(i, i ** 2, color='red')  
        elif i % 3 == 0 or i == -1:  
            plt.scatter(i, i ** 2, color='green')  
        else:  
            plt.scatter(i, i ** 2, color='blue')  

    plt.xlabel('x')  
    plt.ylabel('y')  
    plt.title('Highlight Titik-titik pada Plot Fungsi Kuadrat')  
    plt.grid(True)  
    plt.legend()  
    plt.show()  

# Panggil fungsi untuk menghasilkan plot fungsi kuadrat
plot_kuadrat()

# Panggil fungsi untuk menyoroti titik-titik yang memenuhi kondisi tertentu
highlight_points()
