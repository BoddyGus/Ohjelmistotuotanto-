Agent poisti toisteisuuden melko järkevästi siirtämällä mock-olioiden ja tuotteiden alustuksen setUp-metodiin sekä ostotapahtuman apumetodiin osta_tuotteita.

Testikoodi on helpommin luettavaa: jokainen testi keskittyy enää omaan ostosskenaarioonsa.

Agent ei heikentänyt tarkistuksia. Se säilytti alkuperäisen assert_called()-tarkistuksen ja lisäsi muissa testeissä tarkemmat assert_called_with()-tarkistukset.

Jouduin tarkistamaan erityisesti lopputuotteen loppu -testin, koska setUp-metodin varastoasetukset muutettiin. Agent ylikirjoitti kuitenkin saldon testissä oikein niin, että tuote 1 on saatavilla ja tuote 2 ei.

Yhteenvetona agentin muutos oli sopiva ja testien toiminnallisuus säilyi.