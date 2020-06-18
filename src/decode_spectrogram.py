import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

DTFT_dials = np.array(
    [[697,1209], # 1
     [697,1336], # 2
     [697,1477], # 3
     [770,1209], # 4
     [770,1336], # 5
     [770,1477], # 6
     [852,1209], # 7
     [852,1336], # 8
     [852,1477], # 9
     [941,1209], # *
     [941,1336], # 0
     [941,1477]] # #
)

telephone_keypad = ["{}".format(i) for i in range(1,10)] + ["*","0","#"]


def distDTFT(DTFT_dials, cent):
    return (np.sum((DTFT_dials - cent) ** 2, axis=1))


def decode_spectrogram(freqs, bins, Sxx):
    ifreqs, ibins = np.where(np.log10(Sxx)*10 > -50)
    bins_tone = bins[ibins]
    freqs_tone = freqs[ifreqs]
    pick = freqs_tone > 500
    X = np.array([bins_tone[pick],
                  freqs_tone[pick]]).T

    # for icoord in range(X.shape[0]):
    #     print("Time ={:4.2f}sec, Frequency={:5.2f}Hz".format(*X[icoord, :]))

    Xcolstd = np.std(X, axis=0)
    X_scale = X / Xcolstd

    km = KMeans(n_clusters=22)
    km.fit(X_scale)

    y_pred = km.predict(X_scale)

    # plt.scatter(X[:, 0], X[:, 1], c=y_pred)
    # plt.xlabel("Time (sec)")
    # plt.ylabel("Frequencies (Hz)")
    # plt.show()

    ccenter = km.cluster_centers_ * Xcolstd
    ccenter = np.array([np.round(ccenter[:, 0], 2),
                        np.round(ccenter[:, 1], 0)]).T

    ## reorder according to the time (sec)
    ccenter = ccenter[np.argsort(ccenter[:, 0]), :]
    # for icenter in range(ccenter.shape[0]):
    #     print("{:5.2f} sec {:7.0f}Hz".format(ccenter[icenter][0],
    #                                          ccenter[icenter][1]))

    ccenter_xy0 = np.array([ccenter[1::2, 1],
                            ccenter[::2, 1]]).T

    ccenter_xy = []
    for icenter in range(ccenter_xy0.shape[0]):
        ccenter_xy.append(np.sort(ccenter_xy0[icenter]))
    ccenter_xy = np.array(ccenter_xy)
    print(ccenter_xy)
    print("")

    freq = []
    for icenter in range(ccenter_xy.shape[0]):
        cent = ccenter_xy[icenter]
        dist2center = distDTFT(DTFT_dials, cent)
        i = np.argmin(dist2center)
        freq.append(telephone_keypad[i])

    for i, f in enumerate(freq, 1):
        print("{:02} przycisk = {}".format(i, f))


