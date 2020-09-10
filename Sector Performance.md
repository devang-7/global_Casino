We have to buy stocks in accordance with the sector performance. Hence, we can plot historgrams for the sector performance.

    from alpha_vantage.sectorperformance import SectorPerformances
    import matplotlib.pyplot as plt
    sp = SectorPerformances(key='YOUR_API_KEY', output_format='pandas')
    data, meta_data = sp.get_sector()
    data['Rank A: Real-Time Performance'].plot(kind='bar')
    plt.title('Real Time Performance (%) per Sector')
    plt.tight_layout()
    plt.grid()
    plt.show()
