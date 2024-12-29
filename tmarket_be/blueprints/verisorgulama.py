from flask import request, abort
from flask_restful.inputs import date
from sqlalchemy import Select, inspect


def sorgula(sorgu: Select, dp_sinifi: type, sayfa_no: int = 0, kayit_sayisi: int = 10):
    sorgu = sorgu.limit(kayit_sayisi)
    sorgu = sorgu.offset(sayfa_no * kayit_sayisi)

    siralama_alanlari = request.args.getlist("sirala")
    sutunlar = [col.key for col in inspect(dp_sinifi).mapper.column_attrs]
    for alan_adi in siralama_alanlari:
        if alan_adi.startswith('ar'):
            gercek_alan_adi = alan_adi[3:]
            sorgu = sorgu.order_by(getattr(dp_sinifi, gercek_alan_adi).asc())
        elif alan_adi.startswith('az'):
            gercek_alan_adi = alan_adi[3:]
            sorgu = sorgu.order_by(getattr(dp_sinifi, gercek_alan_adi).desc())

    filtre = request.args.getlist("f")
    if len(filtre) > 0:

        operator_karakterleri = list('<>=!|~')
        ayrilmis_filtre = []
        for filtre_metni in filtre:
            alan_adi = []
            operator = []
            deger = []
            adim = 0
            for karakter in filtre_metni:
                if adim == 0 and karakter not in operator_karakterleri:
                    alan_adi.append(karakter)
                elif adim == 0 and karakter in operator_karakterleri:
                    adim = 1
                    operator.append(karakter)
                elif adim == 1 and karakter in operator_karakterleri:
                    operator.append(karakter)
                elif adim == 1 and karakter not in operator_karakterleri:
                    adim = 2
                    deger.append(karakter)
                else:
                    deger.append(karakter)
            alan_adi_str = "".join(alan_adi)
            operator_str = "".join(operator)
            deger_str = "".join(deger)
            ayrilmis_filtre.append((alan_adi_str, operator_str, deger_str))
        tablo_alanlari=inspect(alan_adi_str,operator_str,deger_str)
        for alan,op,deger in ayrilmis_filtre:
            tablo_alani=tablo_alanlari[alan].class_attribute
            if tablo_alani.class_attribute.type.pyhton_type[int,float]:
                kabul_edilen_operatorler=['>','>=','<','<=','=','~']
                if op not in kabul_edilen_operatorler:
                    abort(400)
                else:
                    if op=='~':
                        degerler=[float(d) for d in deger.split(',')]
                        sorgu=sorgu.where(tablo_alani.between(degerler(0),degerler(1)))

                    else:
                        if op=='>':
                            sorgu=sorgu.where(tablo_alani>float(deger))
                        elif op=='<':
                            sorgu = sorgu.where(tablo_alani < float(deger))
                        elif op=='>=':
                            sorgu=sorgu.where(tablo_alani>=float(deger))
                        elif op=='<=':
                            sorgu = sorgu.where(tablo_alani <= float(deger))
                        else:
                            sorgu = sorgu.where(tablo_alani == float(deger))

            elif tablo_alani.type.pyhton_type[str]:
                kabul_edilen_operatorler = ['|=', '=|', '|=|','!=', '=!','!=!']
                if op not in kabul_edilen_operatorler:
                    abort(400)
                else:
                    if op == '|=':
                        sorgu = sorgu.where(tablo_alani.starswith(deger))
                    else:
                        if op == '=|':
                            sorgu = sorgu.where(tablo_alani.endswith(deger))
                        elif op == '|=|':
                            sorgu = sorgu.where(tablo_alani.contains(deger))
                        elif op == '!=':
                            sorgu = sorgu.where(tablo_alani.istartswith(deger))
                        elif op == '=!':
                            sorgu = sorgu.where(tablo_alani.isendswith(deger))
                        else:
                            sorgu = sorgu.where(tablo_alani.icontains(deger))

            elif tablo_alani.type.pyhton_type[date]:
                print("ok")


        return sorgu
