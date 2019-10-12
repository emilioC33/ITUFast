// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "EvaluationFunctionLibrary.generated.h"


class UGenomeData;

/**
 * 
 */
UCLASS()
class UNREALRACING_API UEvaluationFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:

	UFUNCTION(BlueprintCallable, Category = "EvaluationHelper")
		static void SortPopulation(TArray<UGenomeData*> Array, TArray<UGenomeData*>& SortedArray);

	UFUNCTION(BlueprintCallable, Category = "EvaluationHelper")
		static void WriteFitness(TArray<UGenomeData*> Population, int32 Generation);
	
private:

	static void WriteToFile(FString filename, FString data);
};
