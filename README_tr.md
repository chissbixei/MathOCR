Öncelikle bu proje tam otamatik bir sistem değildir, burdaki bilgilere hakim olmalı ve kullanım klavuzuna uyarak kullanmalısınız. 

Sistem masa üstünde bir klasör olucak şekilde tasarlanıp çalışmaktadır, farklı yere taşımanız halinde çalışmayacaktır.

PİP'LER: `pip install.bat` dosyasını çalıştırırsanız projeyi kullanmak için gerekli tüm pip'ler indirilicektir, bu işlem biraz uzun sürebilir. ilk projem olduğu için çok fazla deneme yanılma yaşadım birkaç kere pip'leri sıfırladım ancak araya gereksiz pipler karışmış olabilir, anlayan birisiyseniz `requirements_full.txt`'nin içerisindeki piplerin gereksiz olanlarını silebilirsiniz.

OCR AŞAMASI İLK ADIM: Başlamadan önce 5 sayfalık pdf'ler üzerinde denemeler yapın, burada sisteminizi test ediyoruz, denemeler sonucunda 5 sayfalık pdf'in işlenme süresine göre pdf'leri işleme sokuyoruz. (5 sayfalık pdf'i işleyemiyecek kadar düşük bir sisteminiz varsa sorun değil okumaya devam edin)

DİKKAT: Sistem eğer 1 pdf'i işlerken 30-45 dakika boyunca işlemeyi tamamlayamazsa zaman aşımına uğramaktadır.

PEKİ NE YAPICAM: Mesela sistem 5 sayfalık pdf'i 10 dakikada tamamladıysa max 15 sayfalık pdf'ler ile işlem yapın, aksi taktirde sistem zaman aşımına uğrar, büyük pdf'leri bölmeye ihtiyacınız varsa bir sonraki maddeyi okuyun.

PDF BÖLME 1: `split` klasörüne girin, bölmek istediğiniz pdf'leri `split_input` adlı klasöre yerleştirin ve `split.bat` adlı dosyayı çalıştırın, bu işlem varsayılan olarak pdf'leri 5'er sayfa olucak şekilde `split_output` klasörüne yükleyecektir, buradan alıp kullanım klavuzunda da belirtilen `input_math` veya `input_text` klasörüne yerleştirin ve kullanım klavuzundaki adımları takip edin, burda elle taşıma yapmamızın sebebi dosya içeriğinin henüz sistem tarafından bilinmemesi.

PDF BÖLME 2: Donanımınıza göre bölünen sayfa sayısını `split_pdf.py` dosyasının içinde 15. ve 16. satırdaki yönlendirmeleri yaparak değiştirebilirsiniz, düşük donanımlı bir bilgisayar için 1'e kadar düşürülebilir, yüksek donanımlı bir bilgisayar için 15-20 belki daha büyük sayılar yazılabilir.

CPU KULLANIMI %100 !!!: Eğer CPU kullanımınız %100'lere çıkarsa `ocr math.bat` dosyasının içindeki yönlendirmeleri takip edip cpu kullanım sınırlaması yapabilirsiniz.

ÖNEMLİ: OCR işleminin en başında taranırken veya bölme işlemine sokulurken eklenen pdf'ler, anlık çökmeler, cmd'yi kapatıp işlemi yarıda kesilmesi ve benzeri durumlarda çıktı alınamayacağı için `input_math`, `input_text` ve `split_input` dosyalarının içerisindeki pdf'ler silinmemektedir, kullanıcı çıktıların doğruluğunu onayladıktan sonra silebir, silmelidir. Çünkü dosyaların içindeki pdf'lerin silinmemesi halinde sisteme yeni dosya eklenip çalıştırılması, eski dosyanın TEKRAR OCR edilmesine sebep olucaktır, önemli dosyalarınızı kaybetmemeniz açısından temizleme/silme işlemi tamamen kullanıcıya bırakılmıştır, sistem dosyalarınızı hiçbir şekilde silmez.

---------------------------------------------- KULLANIM KLAVUZU ----------------------------------------------

Taramak istediğiniz PDF matematiksel işlemler içeriyorsa `input_math` klasörünün içerisine pdf'inizi yükleyin

Taramak istediğiniz PDF matematiksel işlemler içermiyorsa `input_text` klasörünün içerisine pdf'inizi yükleyin

Yükleme yaptığınızı dosya türüne göre `ocr math.bat` dosyasını veya `ocr text.bat` dosyasını çalıştırın.

OCR edilen dosyalar `output_all` klasörüne gelicektir.

Bizim için önemli olan `output_all\%OCR Processed File%\hybrid_auto` içerisindeki `.md` uzantılı Markdown dosyası.

Eğer PDF bölme işlemi yaptıysanız `merge` klasörüne gidip `merge_markdowns.bat` dosyasını çalıştırmanız yeterli olucaktır, sistem otomatik olarak aynı isme sahip klasörleri tespit edip sayfa sırasına göre tekrardan birleştiricektir, birleştirme işleminde kullanılan dosyalar `Processed OCR Folders` klasörüne taşınacaktır, hassas çalışmadığı için dosyalar kullanıcı kontrolünden geçtikten sonra silinebilir.

Merge aşamasını tamamladığınızda `output_all` dosyasının içerisinde split edilmemiş PDF'lerin dosya çıktıları ve text tabanlı ocr çıktıları kalmış olucak, bütün Markdown'ları, OCR çıktı klasörlerini, inputtaki eski klasörleri tek bir yerde toplamak için en son `collect.bat` dosyasını çalıştırın.

Eğer işlemleri doğru yaptıysanız....

Bütün Markdown'lar `All Markdowns` klasörüne
(output_all içindeki .md'ler ------ output_all\***** içidneki .md'ler ------ merge\Merged Markdowns içindeki .md'ler)

Bütün input pdf'leri `Processed Inputs` klasörüne
(input_math - input_text - split_input)

Bütün işlenmiş çıktılar `Processed OCR Folders` klasörüne
(output_all içinde kalan klasörler)

OCR işlemini tamamladıktan sonra diğer dosya olan `rag_sistemi` dosyası ile chunklama, embedding vs ile devam edebilirsiniz. `Henüz geliştirme aşamasında`

Oraya ait `README.md` dosyasını da okuyunuz.