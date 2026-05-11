# Το παρακάτω πρόγραμμα διαβάζει τους βαθμούς ενός μαθητή σε τέσσερα (4) μαθήματα. Δέχεται δύο τιμές, μία για τη γραπτή και μία για την προφορική εξέταση, υπολογίζει τον Μ.Ο. (Μέσο Όρο) κάθε μαθήματος, τον αποθηκεύει σε μία γενική λίστα, υπολογίζει τον Γ.Μ.Ο. (Γενικό Μέσο Όρο) και εμφανίζει το εάν πέρασε ή όχι.

BASH_MATHIMATON = 10
bathmoi = []

# Ζητάει βαθμούς και κάνει έλεγχο ορθότητας τιμών για 4 μαθήματα. (Οι βαθμοί κυμαίνονται ανάμεσα του 0 και του 20).
for i in range (0,4):
    mathima = input(f"---- Εισαγωγή για το {i+1} μάθημα ----")
    bathmos_graptou = float(input("Τι βαθμό είχες στο γραπτό κομμάτι της εξετάσεως;"))
    while bathmos_graptou < 0 or bathmos_graptou > 20:
        bathmos_graptou = float(input("Τι βαθμό είχες στο γραπτό κομμάτι της εξετάσεως; (Η τιμή πρέπει να κυμαίνεται μεταξύ 0 και 20)"))

    bathmos_proforikou = float(input("Τι βαθμό είχες στο προφορικό κομμάτι της εξετάσεως;"))
    while bathmos_proforikou < 0 or bathmos_proforikou > 20:
        bathmos_proforikou = float(input("Τι βαθμό είχες στο προφορικό κομμάτι της εξέτασεως; (Η τιμή πρέπει να κυμαίνεται μεταξύ 0 και 20)"))

    # Υπολογισμός μέσου όρου και έλεγχος επιτυχίας

    mesos_oros = (bathmos_graptou + bathmos_proforikou) / 2
    print (f"Στο μάθημα: {mathima} ο Μ.Ο. σου είναι: {mesos_oros}")
    bathmoi.append(mesos_oros)

gen_mesos_oros = sum(bathmoi) / len(bathmoi)
if gen_mesos_oros >= BASH_MATHIMATON:
    print(f"Εφόσον ο Γ.Μ.Ο. είναι παραπάνω του 10 ({gen_mesos_oros}), περνάς!")
else:
    print(f"Δυστυχώς ο Γ.Μ.Ο. σου είναι μικρότερος της βάσης ({gen_mesos_oros}). Έμεινες!")